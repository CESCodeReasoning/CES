## Instruction to run CES:
```cd scripts/ces```

```python/run.py --model $MODEL_ID --dataset humaneval --cache $CACHE_DIR```

```MODEL_ID```: Currently our framework supports following OpenAI and huggingface models:  ```codellama/CodeLlama-13b-Instruct-hf```, ```codellama/CodeLlama-13b-hf```,  ```codellama/CodeLlama-13b-Instruct-hf```,```codellama/CodeLlama-7b-hf```,  ```codellama/CodeLlama-7b-Instruct-hf```, ```codellama/CodeLlama-34b-Instruct-hf``` ```codellama/CodeLlama-13b-hf```,```deepseek-ai/deepseek-coder-6.7b-instruct```, ```deepseek-ai/deepseek-coder-33b-instruct```,```deepseek-ai/deepseek-coder-6.7b-base```, ```ise-uiuc/Magicoder-S-DS-6.7B```, ```bigcode/starcoder```, ```bigcode/starcoder2-15b```, ```gpt-4-turbo```,
```gemini/gemini-1.5-pro```, ```semcoder/semcoder_s```

```CACHE_DIR```: the directory to save huggingface checkpoints.
## Instruction to run LLMs on bug prediction:
```cd scripts/bp```

```python/bp.py --model $MODEL_ID --dataset humaneval --cache $CACHE_DIR```


## Instruction to run LLMs on bug localization:
```cd scripts/bl```

```python/bl.py --model $MODEL_ID --dataset humaneval --cache $CACHE_DIR```



## Instruction to run LLMs on bug repair:
```cd scripts/br```

```python/apr.py --model $MODEL_ID --dataset humaneval --cache $CACHE_DIR```

