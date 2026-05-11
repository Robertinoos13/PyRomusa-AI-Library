def use_engine(bot_instance, prompt: str, 
            sensitivity: int = 1, 
            with_memory: bool = True, 
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
    from collections import defaultdict

    def strip_diacritics(s: str) -> str:
        return ''.join(
            ch for ch in unicodedata.normalize('NFKD', str(s))
            if not unicodedata.combining(ch)
        ).lower()

    def normalize_text(s: str) -> str:
        return re.sub(r"\s+", " ", strip_diacritics(s)).strip()

    def tokenize(text: str):
        return [t for t in re.findall(r"\w+|[^\w\s]", normalize_text(text), flags=re.UNICODE) if t.strip()]

    def sentence_case(text: str) -> str:
        text = re.sub(r"\s+", " ", str(text)).strip()
        if not text:
            return text
        return text[0].upper() + text[1:]

    def cleanup_spacing(text: str) -> str:
        text = re.sub(r"\s+([,.;:!?…])", r"\1", text)
        text = re.sub(r"([(\[])\s+", r"\1", text)
        text = re.sub(r"\s{2,}", " ", text)
        return text.strip()

    def fallback_by_language(kind: str) -> str:
        fb = normalize_text(fallback_language)
        # Definire mesaje fallback
        if kind == "empty":
            if fb in ("romanian", "romana", "română", "rom"): return fallback_empty_string_message or "Te ascult..."
            if fb in ("english", "engleza", "engleză", "eng"): return fallback_empty_string_message or "I am listening to you..."
            if fb in ("spanish", "spaniola", "spaniolă", "spa"): return fallback_empty_string_message or "Te estoy escuchando..."
            return fallback_empty_string_message or ""
        
        if kind in ("not_understood", "not_sure"):
            if fb in ("romanian", "romana", "română", "rom"): return fallback_no_understanded_message or "Nu sunt sigur că am înțeles, dar sună interesant!"
            if fb in ("english", "engleza", "engleză", "eng"): return fallback_no_understanded_message or "I'm not sure if I understand, but it sounds interesting!"
            if fb in ("spanish", "spaniola", "spaniolă", "spa"): return fallback_no_understanded_message or "No estoy seguro si lo entiendo, pero ¡suena interesante!"
            return fallback_no_understanded_message or ""
        return ""

    def detect_intent(words, raw_prompt: str) -> str:
        raw = normalize_text(raw_prompt)
        joined = " ".join(words)
        
        greeting_hits = {"salut", "buna", "hello", "hey", "yo", "hi", "neata"}
        if any(w in joined for w in greeting_hits): return "greeting"
        if any(x in raw for x in ("ce este", "ce e", "cum", "de ce", "explica", "what is", "how", "why")): return "explanation"
        if any(x in raw for x in ("ce sa fac", "ajutor", "help", "sugere")): return "advice"
        if any(x in raw for x in ("trist", "fericit", "confuz", "frustr", "stres", "obosit", "suparat", "sad", "angry")): return "emotional"
        if any(x in raw for x in ("cat", "calculeaza", "+", "-", "x", "/", "impart")): return "math"
        if "?" in raw_prompt: return "question"
        return "generic"

    def build_response_from_ids(ids):
        words = [id_to_word.get(i, "") for i in ids if id_to_word.get(i, "")]
        return cleanup_spacing(" ".join(words))

    total_vocab = getattr(bot_instance, "total_vocabulary", {}) or {}
    dataset = getattr(bot_instance, "translated_input_and_output_examples", []) or []

    if show_thinking:
        print(f"[START THINKING]\nI received the prompt: {prompt!r}")

    if not total_vocab or not dataset:
        resp = fallback_by_language("not_understood")
        if with_memory:
            bot_instance.last_user_prompt = str(prompt)
            bot_instance.last_bot_output = resp
        return resp

    id_to_word = getattr(bot_instance, "id_to_word", None) or {v: k for k, v in total_vocab.items()}
    norm_vocab = {normalize_text(word): wid for word, wid in total_vocab.items() if normalize_text(word)}

    def word_to_id(word: str): return norm_vocab.get(normalize_text(word))

    words = tokenize(prompt)
    if not words:
        resp = fallback_by_language("empty")
        if with_memory:
            bot_instance.last_user_prompt = str(prompt)
            bot_instance.last_bot_output = resp
        return resp

    prompt_ids = [word_to_id(w) for w in words if word_to_id(w) is not None]
    prompt_id_set = set(prompt_ids)
    prompt_norm_set = {normalize_text(w) for w in words if normalize_text(w)}

    if not prompt_ids and not prompt_norm_set:
        resp = fallback_by_language("not_understood")
        if with_memory:
            bot_instance.last_user_prompt = str(prompt)
            bot_instance.last_bot_output = resp
        return resp

    # --- Algoritm TF-IDF pentru precizie maximă ---
    doc_freq = defaultdict(int)
    total_docs = len(dataset)
    for ex in dataset:
        for w in ex.get("input_words", set()):
            doc_freq[w] += 1

    def get_idf(word):
        df = doc_freq.get(word, 0)
        # Cuvintele rare primesc scor enorm, cuvintele dese (ce, este, un) sunt penalizate
        return math.log(total_docs / (1 + df)) + 1.0

    last_user_set = set(tokenize(getattr(bot_instance, "last_user_prompt", ""))) if with_memory else set()
    last_bot_set = set(tokenize(getattr(bot_instance, "last_bot_output", ""))) if with_memory else set()

    sens = max(1.0, float(sensitivity) if str(sensitivity).replace('.','',1).isdigit() else 1.0)
    intent = detect_intent(words, prompt)

    scored = []
    
    # --- PROCES DE SCORARE ÎMBUNĂTĂȚIT ---
    for ex in dataset:
        ex_in_ids = ex.get("input_ids", []) or []
        ex_in_set = set(ex_in_ids)
        ex_in_words = {normalize_text(w) for w in ex.get("input_words", []) or [] if w}
        ex_out_ids = ex.get("output_ids", []) or []

        if not ex_in_ids and not ex_in_words: continue

        # Context Logic
        has_condition = bool(ex.get("if_last_input_words")) or bool(ex.get("if_last_output_words"))
        context_total = 0
        if has_condition and with_memory:
            context_total += len((ex.get("if_last_input_words") or set()).intersection(last_user_set))
            context_total += len((ex.get("if_last_output_words") or set()).intersection(last_bot_set))
            if context_total < sens: continue

        matched_words = prompt_norm_set.intersection(ex_in_words)
        if not matched_words: continue

        # Calculare scor inteligent: bazat pe importanța statistică a cuvântului (TF-IDF)
        idf_score = sum(get_idf(w) for w in matched_words)
        
        score = 0.0
        score += idf_score * 4.0 # Forța principală este importanța logică a cuvântului
        score += len(matched_words) * 1.5
        score += 1.2 * context_total
        
        # Penalizează răspunsurile care sunt prea lungi/scurte față de promptul cerut
        len_diff_penalty = abs(len(ex_in_set) - len(prompt_id_set)) * 0.1
        score -= len_diff_penalty

        out_text = build_response_from_ids(ex_out_ids).lower()
        if intent == "explanation" and any(w in out_text for w in ("este", "înseamnă", "ajută", "is", "means")): score += 1.0
        elif intent == "advice" and any(w in out_text for w in ("ar trebui", "poți", "recomand", "should")): score += 1.0
        elif intent == "emotional" and any(w in out_text for w in ("înțeleg", "calm", "aici", "understand")): score += 1.0

        if score > 0:
            scored.append((score, ex_out_ids, ex))

        # Calculare scor inteligent: bazat pe importanța statistică a cuvântului (TF-IDF)
        idf_score = sum(get_idf(w) for w in matched_words)
        
        score = 0.0
        score += idf_score * 4.0 # Forța principală este importanța logică a cuvântului
        score += len(matched_words) * 1.5
        score += 1.2 * context_total
        
        # Penalizează răspunsurile care sunt prea lungi/scurte față de promptul cerut
        len_diff_penalty = abs(len(ex_in_set) - len(prompt_id_set)) * 0.1
        score -= len_diff_penalty

        out_text = build_response_from_ids(ex_out_ids).lower()
        if intent == "explanation" and any(w in out_text for w in ("este", "înseamnă", "ajută", "is", "means")): score += 1.0
        elif intent == "advice" and any(w in out_text for w in ("ar trebui", "poți", "recomand", "should")): score += 1.0
        elif intent == "emotional" and any(w in out_text for w in ("înțeleg", "calm", "aici", "understand")): score += 1.0

        if score > 0:
            scored.append((score, ex_out_ids, ex))

    if not scored:
        resp = fallback_by_language("not_sure")
        if with_memory:
            bot_instance.last_user_prompt = str(prompt)
            bot_instance.last_bot_output = resp
        return resp

    scored.sort(key=lambda x: x[0], reverse=True)
    best_score = scored[0][0]
    
    # Setăm un prag minim logic bazat pe cel mai bun scor
    top_candidates = [c for c in scored if c[0] >= best_score * 0.7][:5]

    try: temp = float(temperature)
    except Exception: temp = 0.0

    # --- NOU: Sinteză Generativă (Simulare comportament LLM) ---
    def generate_mini_llm_response(candidates, temperature, base_intent):
        best_text = build_response_from_ids(candidates[0][1]).strip()
        
        if temperature <= 0.01 or len(candidates) == 1:
            return best_text # Returnare exactă pentru precizie 100%
            
        # Dacă temperatura e mai mare, generăm un răspuns combinând logic structuri din top
        # Extragem alte texte relevante
        alt_texts = [build_response_from_ids(c[1]).strip() for c in candidates[1:3]]
        
        intro_pool = {
            "explanation": ["Din câte știu,", "Pe scurt,", "Iată o explicație:", "Practic,"],
            "advice": ["O idee ar fi să", "Aș sugera să", "Poate ar ajuta dacă"],
            "generic": ["Uite cum stă treaba:", "În principiu,", "Să știi că"]
        }
        
        # Generare hibridă: Alegem un intro dinamic bazat pe intenție
        dynamic_intro = ""
        if random.random() < (temperature * 1.5) and base_intent in intro_pool:
            dynamic_intro = random.choice(intro_pool[base_intent]) + " "
            
        # Dacă găsim o a doua propoziție relevantă, o lipim (simulare context extins)
        extra_context = ""
        if alt_texts and random.random() < temperature:
            second_best = alt_texts[0]
            # Evităm să repetăm aceeași idee
            if len(set(best_text.split()) & set(second_best.split())) < (len(best_text.split()) * 0.6):
                # Extragem prima parte logică a celui de-al doilea răspuns
                parts = re.split(r'[,.!?;]', second_best)
                if len(parts[0]) > 10:
                    extra_context = " De asemenea, " + parts[0].strip().lower() + "."

        final_gen = dynamic_intro + best_text[0].lower() + best_text[1:] if dynamic_intro else best_text
        final_gen += extra_context
        
        return final_gen

    # Aplicăm noul mecanism de generare
    response = generate_mini_llm_response(top_candidates, temp, intent)
    response = cleanup_spacing(response)
    response = sentence_case(response)

    if response and response[-1] not in ".!?,;:…" and len(response.split()) > 2:
        response += "."

    if show_thinking:
        print(f"Best TF-IDF Score: {best_score:.4f}")
        print(f"Chosen response: {response!r}")
        print("[STOP THINKING]\n---")

    if show_debug:
        print("--- [START DEBUG] ---")
        print(f"prompt: {prompt}")
        print(f"intent: {intent}")
        print(f"best TF-IDF score: {best_score}")
        print(f"top_candidates (score, text): {[(round(s, 2), build_response_from_ids(ids)[:30]+'...') for s, ids, _ in top_candidates]}")
        print(f"final generated response: {response}")
        print("--- [STOP DEBUG] ---")

    if with_memory:
        bot_instance.last_user_prompt = str(prompt)
        bot_instance.last_bot_output = response

    return response