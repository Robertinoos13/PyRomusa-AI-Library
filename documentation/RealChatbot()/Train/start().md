# `bot.trainer.start()`

## Description

Start training the chatbot so that, once invoked, it can generate human-like text based on the input prompt. This is a useful function once you have loaded your training data and are ready to tackle the most demanding task for your hardware: training a small LLM on text.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`epochs`|This determines how many times you want the chatbot to see the same training examples so it performs better on them. It also affects the total training time.|`100`|
|`show_loss_every_x_epochs`|Specify at approximately how many epochs the loss process should be displayed.|`10`|
|`show_loss_process`|Specifies whether to display (`True`) or not display (`False`) the current loss process, regardless of the `show_loss_every_x_epochs` value.|`True`|
|`use_gpu_if_is_available`|Specifies whether training is allowed to use your graphics card (`True`) or only the CPU (`False`). If you do not have a dedicated GPU, training will proceed as if this parameter were set to `False`. This affects the total training duration and the hardware load on specific components.|`True`|
|`learn_rate`|How aggressively should the chatbot modify its parameters after completing an epoch?|`1e-3`|
|`min_learn_rate`|Specify the minimum learning rate the chatbot can reach.|`1e-5`|
|`batch_size`|It specifies how many training examples (a training example being defined in tokens as `max_len * batch_size`) to process simultaneously before calculating the error and making a decision. A lower value results in more noise and lower hardware efficiency, whereas a higher value offers greater stability and better hardware efficiency.|`32`|
|`ask_to_stop_every_x_epochs`|Pause the training every certain number of epochs so you can be asked whether you wish to continue training or stop it altogether.|`0`|
|`auto_checkpoint_every_x_epochs`|Automatically save the chatbot to a `.pt` file during training. This file can be updated every set number of epochs.|`0`|
|`checkpoint_file_name`|Specify the filename under which the chatbot should be automatically saved while training is running.|`my_chatbot_checkpoint`|
|`checkpoint_file_location`|Specify the filepath under which the chatbot should be automatically saved while training is running.|`""`|
|`fine_tune_only_new_data`|Regarding training on new examples, specify whether you want to adapt strictly to the new training data (which is less stable) or train it as if starting from scratch (which takes longer but is more stable).|`True`|
|`freeze_base_layers`|Specify if you do not wish to modify certain parts of the chatbot's architecture. Leave the value as `None` if you want the decision to be made automatically based on the situation.|`None` (if modify manually, needs a `boolean` value)|
|`show_suplimentary_info_in_console`|Specify whether you want to see less important details in the output.|`False`|


## Returns

- **value type(s):** string
- **number of values returned per call:** ???
- **It needs an additional `print()` function:** no

## Codes examples

``` python
from pyromusa_ai import RealChatbot

# We configure the chatbot to understand only whole words, thereby making the training process shorter compared to a char-level approach.
bot = RealChatbot(tokenizer_type="word-level")

# We are loading the smallest prepared dataset in English.
bot.prepared_datasets.english.load_prepared_dataset("low")

"""
The moment of truth: 
Why is the `bot.trainer.start()` function so important? 
↓↓↓
"""

# We are testing our chatbot before training. (WARNING message)
print(f"BOT: {bot.reply_at(prompt=input("USER: "))}")

# We begin training. We set a lower number of epochs to finish the training faster.
bot.trainer.start(epochs=10)

# We are testing our chatbot after training. (Works normally)
print(f"BOT: {bot.reply_at(prompt=input("USER: "))}")
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_