# Tokenization
Let's build a GPT Tokenizer!

This repository is a simple implementation of the **Byte Pair Encoding Algorith**m in Tokenization for LLMs. 

`lecture.ipynb` is the note from [Andrej Karpathy's Tutorial](https://www.youtube.com/watch?v=zduSFxRajkE&t=2s), which covers the general **BPE Algorithm**, GPT Tokenization, [sentencepiece tokenizer by google](https://github.com/google/sentencepiece) used by Llama2 and Mistral, and papers including [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/pdf/2207.14255) and [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

Visualization for tokenizers can be found from [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/?encoder=cl100k_base).

The implementation of the `base.py`, `basic.py`, and `regex.py` references the [minbpe repository](https://github.com/karpathy/minbpe/tree/master), 
which represents the generic tokenizer, the basic tokenizer with **BPE Algorithm**, and the regex tokenizer similar to what [OpenAI's Tiktoken for GPT4](https://github.com/openai/tiktoken)
and [GPT2 Tokenizer](https://github.com/openai/gpt-2/blob/master/src/encoder.py) is made from.

The basic bpe tokenizer outputs the following result:

<img width="1131" alt="Screenshot 2024-07-10 at 11 29 19 AM" src="https://github.com/yebyyy/Tokenization/assets/144394157/60551325-afce-4abb-bc8a-e2eddac7758d">

The GPT4 tokenizer outouts the following result:

<img width="1290" alt="Screenshot 2024-07-10 at 1 54 12 PM" src="https://github.com/yebyyy/Tokenization/assets/144394157/fcb02285-aebc-4141-8d3e-ee6d8cad330e">

