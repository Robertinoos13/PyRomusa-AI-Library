def use_engine(bot_instance, prompt: str,
            sensitivity: int = 1,
            with_memory: bool = True,
            max_inflenced_memory: int = 3,
            new_lines_system: bool = True,
            fallback_language="english",
            fallback_empty_string_message="",
            fallback_no_understanded_message="",
            fallback_not_sure_message="",
            temperature: float = 0.0,
            show_thinking=False,
            allow_long_text_thinking=True,
            show_debug=False):

    import math
    import random
    import re
    import unicodedata
    from collections import Counter, defaultdict

    NEW_LINE_TOKEN = getattr(bot_instance, "_new_line_token", "__PYROMUSA_NEW_LINE__")

    def format_new_lines(text):
        if hasattr(bot_instance, "_decode_new_lines"):
            return bot_instance._decode_new_lines(text, new_lines_system=new_lines_system)
        return text

    def strip_diacritics(text):
        return "".join(
            ch for ch in unicodedata.normalize("NFKD", str(text))
            if not unicodedata.combining(ch)
        ).lower()

    def normalize(text):
        return re.sub(r"\s+", " ", strip_diacritics(text)).strip()

    def word_tokens(text):
        if hasattr(bot_instance, "_encode_new_lines"):
            text = bot_instance._encode_new_lines(text)
        return [
            normalize(token)
            for token in re.findall(r"\w+", str(text), flags=re.UNICODE)
            if normalize(token) and normalize(token) != normalize(NEW_LINE_TOKEN)
        ]

    def visible_tokens(text):
        if hasattr(bot_instance, "_encode_new_lines"):
            text = bot_instance._encode_new_lines(text)
        return re.findall(r"\w+|[^\w\s]+", str(text), flags=re.UNICODE)

    def cleanup_spacing(text):
        text = str(text)
        text = re.sub(r"\s+([,.;:!?])", r"\1", text)
        text = re.sub(r"([(\[{])\s+", r"\1", text)
        text = re.sub(r"\s+([)\]}])", r"\1", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
        return text.strip()

    def sentence_case(text):
        text = cleanup_spacing(text)
        for index, char in enumerate(text):
            if char.isalpha():
                return text[:index] + char.upper() + text[index + 1:]
        return text

    def fallback_by_language(kind):
        fb = normalize(fallback_language)
        if kind == "empty":
            if fb in ("romanian", "romana", "rom"):
                return fallback_empty_string_message or "Te ascult..."
            if fb in ("spanish", "spaniola", "spa"):
                return fallback_empty_string_message or "Te estoy escuchando..."
            return fallback_empty_string_message or "I am listening to you..."

        if fb in ("romanian", "romana", "rom"):
            return fallback_no_understanded_message or fallback_not_sure_message or "Nu sunt sigur ca am inteles, dar suna interesant!"
        if fb in ("spanish", "spaniola", "spa"):
            return fallback_no_understanded_message or fallback_not_sure_message or "No estoy seguro si lo entiendo, pero suena interesante!"
        return fallback_no_understanded_message or fallback_not_sure_message or "I'm not sure if I understand, but it sounds interesting!"

    def debug(name, value):
        if show_debug:
            print(f"[DEBUG] {name}: {value}")

    def thinking(message):
        if show_thinking:
            if allow_long_text_thinking:
                print(f"[THINKING] {message}")
            else:
                print(f"[THINKING] {str(message)[:180]}")

    def raw_samples():
        samples = []
        for sample in getattr(bot_instance, "training_dataset", []) or []:
            if isinstance(sample, dict):
                inp = str(sample.get("input", ""))
                out = str(sample.get("output", ""))
                if_last_in = sample.get("if_last_input")
                if_last_out = sample.get("if_last_output")
            elif isinstance(sample, (list, tuple)):
                inp = str(sample[0]) if len(sample) > 0 else ""
                out = str(sample[1]) if len(sample) > 1 else ""
                if_last_in = sample[2] if len(sample) > 2 else None
                if_last_out = sample[3] if len(sample) > 3 else None
            else:
                inp = str(sample)
                out = ""
                if_last_in = None
                if_last_out = None

            if inp or out:
                samples.append({
                    "input": inp,
                    "output": out,
                    "if_last_input": if_last_in,
                    "if_last_output": if_last_out,
                    "input_words": set(word_tokens(inp)),
                    "output_words": set(word_tokens(out)),
                })
        return samples

    def choose_by_temperature(candidates):
        if not candidates:
            return None
        try:
            temp = float(temperature)
        except Exception:
            temp = 0.0
        if temp <= 0.0:
            return max(candidates, key=lambda item: item[0])[1]

        top = sorted(candidates, key=lambda item: item[0], reverse=True)[:8]
        max_score = max(score for score, _ in top)
        weights = [math.exp((score - max_score) / max(temp, 0.05)) for score, _ in top]
        return random.choices([item for _, item in top], weights=weights, k=1)[0]

    prompt_words = word_tokens(prompt)
    prompt_word_set = set(prompt_words)
    if not prompt_words:
        return format_new_lines(fallback_by_language("empty"))

    samples = raw_samples()
    if not samples:
        return format_new_lines(fallback_by_language("not_understood"))

    doc_freq = defaultdict(int)
    for sample in samples:
        for word in sample["input_words"] | sample["output_words"]:
            doc_freq[word] += 1

    total_docs = max(1, len(samples))

    def idf(word):
        return math.log((total_docs + 1) / (doc_freq.get(word, 0) + 1)) + 1.0

    memory_words = set()
    if with_memory and hasattr(bot_instance, "_get_recent_conversation_words"):
        recent_user_words, recent_bot_words = bot_instance._get_recent_conversation_words(max_inflenced_memory)
        memory_words = {normalize(word) for word in recent_user_words + recent_bot_words if normalize(word)}

    def condition_score(sample):
        if not with_memory:
            if sample.get("if_last_input") or sample.get("if_last_output"):
                return None
            return 0.0

        needed_input = set(word_tokens(sample.get("if_last_input") or ""))
        needed_output = set(word_tokens(sample.get("if_last_output") or ""))
        if not needed_input and not needed_output:
            return 0.0

        matches = len((needed_input | needed_output) & memory_words)
        try:
            threshold = max(1, int(float(sensitivity)))
        except Exception:
            threshold = 1
        if matches < threshold:
            return None
        return float(matches) * 1.4

    scored = []
    for sample in samples:
        ctx = condition_score(sample)
        if ctx is None:
            continue

        input_overlap = prompt_word_set & sample["input_words"]
        output_overlap = prompt_word_set & sample["output_words"]
        all_overlap = prompt_word_set & (sample["input_words"] | sample["output_words"])
        if not all_overlap and not ctx:
            continue

        score = ctx
        score += sum(idf(word) for word in input_overlap) * 3.2
        score += sum(idf(word) for word in output_overlap) * 1.4
        score += len(all_overlap) * 0.8

        length_gap = abs(len(prompt_words) - max(1, len(sample["input_words"])))
        score -= min(length_gap * 0.08, 1.2)
        scored.append((score, sample))

    if not scored:
        return format_new_lines(fallback_by_language("not_sure"))

    scored.sort(key=lambda item: item[0], reverse=True)
    best_score = scored[0][0]
    top_samples = [sample for score, sample in scored if score >= max(0.1, best_score * 0.45)][:8]
    training_outputs = {cleanup_spacing(sample["output"]) for sample in samples if sample["output"]}

    if len(top_samples) == 1:
        response = sentence_case(top_samples[0]["output"])
        if show_thinking:
            print("[THINKING] Only one relevant example found; using it directly.")
            print("[STOP THINKING]")
            print("---")
        debug("prompt_words", prompt_words)
        debug("top_samples", [(round(score, 3), sample["input"], sample["output"]) for score, sample in scored[:5]])
        debug("candidate_count", 0)
        debug("response", response)
        return format_new_lines(response)

    word_frequency = Counter()
    original_forms = {}
    for sample in samples:
        for token in visible_tokens(sample["input"] + " " + sample["output"]):
            norm = normalize(token)
            if norm and re.match(r"\w+$", token, flags=re.UNICODE):
                word_frequency[norm] += 1
                original_forms.setdefault(norm, token)

    def concept_score(word):
        norm = normalize(word)
        if not norm:
            return 0.0
        return idf(norm) + min(len(norm), 12) * 0.06 - word_frequency.get(norm, 0) * 0.015

    def concepts_from_prompt():
        concepts = []
        for token in re.findall(r"\w+", str(prompt), flags=re.UNICODE):
            norm = normalize(token)
            if norm and len(norm) >= 2:
                concepts.append((concept_score(norm) + 2.0, token))
        return concepts

    def concepts_from_samples():
        concepts = []
        for rank, sample in enumerate(top_samples):
            rank_bonus = max(0.0, 1.4 - rank * 0.15)
            for source in (sample["input"], sample["output"]):
                for token in re.findall(r"\w+", source, flags=re.UNICODE):
                    norm = normalize(token)
                    if norm and len(norm) >= 3:
                        concepts.append((concept_score(norm) + rank_bonus, token))
        return concepts

    def unique_concepts(items):
        seen = set()
        result = []
        for score, token in sorted(items, key=lambda item: item[0], reverse=True):
            norm = normalize(token)
            if not norm or norm in seen:
                continue
            seen.add(norm)
            result.append((score, token))
        return result

    target_concepts = unique_concepts(concepts_from_prompt() + concepts_from_samples())[:12]

    def replace_word(text, old_norm, new_word):
        parts = visible_tokens(text)
        indexes = [
            index for index, token in enumerate(parts)
            if re.match(r"\w+$", token, flags=re.UNICODE) and normalize(token) == old_norm
        ]
        if not indexes:
            return text
        parts[indexes[-1]] = str(new_word)
        return cleanup_spacing(" ".join(parts))

    def content_words(text):
        result = []
        for token in re.findall(r"\w+", str(text), flags=re.UNICODE):
            norm = normalize(token)
            if len(norm) >= 3 and not norm.isdigit() and norm != normalize(NEW_LINE_TOKEN):
                result.append((norm, token))
        return result

    def replacement_targets(text):
        words = [
            (normalize(token), token)
            for token in visible_tokens(text)
            if re.match(r"\w+$", token, flags=re.UNICODE) and normalize(token)
        ]
        candidates = []
        for index, (norm, _token) in enumerate(words):
            if len(norm) >= 3 and not norm.isdigit() and norm != normalize(NEW_LINE_TOKEN):
                prev_norm = words[index - 1][0] if index > 0 else ""
                next_norm = words[index + 1][0] if index + 1 < len(words) else ""
                # Very short neighboring words often behave like connectors in
                # many languages, so replacing around them tends to sound rough.
                if (prev_norm and len(prev_norm) <= 2) or (next_norm and len(next_norm) <= 2):
                    continue
                candidates.append(norm)

        filtered = [norm for norm in candidates if norm not in prompt_word_set] or candidates
        return filtered[-1:]

    def candidate_quality(text, source_score=0.0, target_score=0.0):
        cleaned = sentence_case(text)
        words = word_tokens(cleaned)
        if len(words) < 2:
            return None

        score = source_score + target_score
        score += len(prompt_word_set & set(words)) * 2.0
        score += min(len(set(words)), 10) * 0.15
        if cleaned not in training_outputs:
            score += 2.5
        if len(words) > 24:
            score -= (len(words) - 24) * 0.12

        repeated = len(words) - len(set(words))
        score -= repeated * 0.35
        return score, cleaned

    candidates = []

    # 1) Template slotting: keep a natural sentence shape, replace one content word
    # with a stronger concept from the prompt or another relevant example.
    for rank, sample in enumerate(top_samples):
        base = sample["output"]
        base_words = content_words(base)
        if not base_words:
            continue
        source_score = max(0.0, 2.0 - rank * 0.18)
        base_norms = {norm for norm, _ in base_words}
        replaceables = replacement_targets(base)

        for target_score, target in target_concepts:
            target_norm = normalize(target)
            if not target_norm or target_norm in base_norms:
                continue
            for old_norm in replaceables:
                candidate = replace_word(base, old_norm, target)
                quality = candidate_quality(candidate, source_score, target_score)
                if quality:
                    candidates.append(quality)

    # 2) Clause weave: join the most relevant sentence fragment with a distinct
    # fragment from another answer, then score for novelty and prompt relevance.
    fragments = []
    for rank, sample in enumerate(top_samples):
        for fragment in re.split(r"(?<=[.!?;])\s+|[\n]+", sample["output"]):
            fragment = cleanup_spacing(fragment)
            if len(word_tokens(fragment)) >= 2:
                fragments.append((max(0.0, 1.5 - rank * 0.12), fragment))

    for left_score, left in fragments[:6]:
        left_words = set(word_tokens(left))
        for right_score, right in fragments[:8]:
            if left == right:
                continue
            right_words = set(word_tokens(right))
            if len(left_words & right_words) > max(1, min(len(left_words), len(right_words)) // 2):
                continue
            combined = cleanup_spacing(left.rstrip(".!?;") + ", " + right[0].lower() + right[1:])
            quality = candidate_quality(combined, left_score + right_score, 0.0)
            if quality:
                candidates.append(quality)

    # 3) If the dataset is tiny, still try to synthesize a compact sentence from
    # a short template and the best available concept.
    if not candidates and target_concepts:
        template_sample = top_samples[0]
        base_words = content_words(template_sample["output"])
        if len(base_words) >= 2:
            target = target_concepts[0][1]
            compact = " ".join([base_words[0][1], base_words[1][1], str(target)])
            quality = candidate_quality(compact, 1.0, target_concepts[0][0])
            if quality:
                candidates.append(quality)

    if candidates:
        response = choose_by_temperature(candidates)
    else:
        response = top_samples[0]["output"]

    response = sentence_case(response)
    if response and response[-1] not in ".!?;:\n" and len(word_tokens(response)) > 2:
        response += "."

    if show_thinking:
        print("[THINKING] Generated response from adaptive templates.")
        print("[STOP THINKING]")
        print("---")

    debug("prompt_words", prompt_words)
    debug("top_samples", [(round(score, 3), sample["input"], sample["output"]) for score, sample in scored[:5]])
    debug("candidate_count", len(candidates))
    debug("response", response)

    return format_new_lines(response)
