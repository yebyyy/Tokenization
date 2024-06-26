# Tokenization
Let's build a GPT Tokenizer!

This repository is a simple implementation of the **Byte Pair Encoding Algorith**m in Tokenization for LLMs. 

`lecture.ipynb` is the note from [Andrej Karpathy's Tutorial](https://www.youtube.com/watch?v=zduSFxRajkE&t=2s), which covers the general **BPE Algorithm**, GPT Tokenization, [sentencepiece tokenizer by google](https://github.com/google/sentencepiece) used by Llama2 and Mistral, and papers including [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/pdf/2207.14255) and [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

Visualization for tokenizers can be found from [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/?encoder=cl100k_base).

The implementation of the `base.py`, `basic.py`, and `regex.py` references the [minbpe repository](https://github.com/karpathy/minbpe/tree/master), 
which represents the generic tokenizer, the basic tokenizer with **BPE Algorithm**, and the regex tokenizer similar to what [OpenAI's Tiktoken for GPT4](https://github.com/openai/tiktoken)
and [GPT2 Tokenizer](https://github.com/openai/gpt-2/blob/master/src/encoder.py) is made from.

