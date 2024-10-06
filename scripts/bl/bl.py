import argparse
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import openai
from tqdm import tqdm
from create_prompt_fl import create_prompt
from prompt import chatgpt_generator, huggingface_generator, huggingface_generator_chat, generator_lllm, generator_gemini, generator_vllm
import json
from vllm import LLM, SamplingParams

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
MAX_NEW_TOKEN=512
def find_path(dataset):
    root = "../dataset/Intermediate/Repair"
    data_path = os.path.join(root, dataset)
    if not os.path.exists(data_path):
        print(f'{data_path} not exists.')
    return data_path

def load_model(model_id, cache_dir, api_type):
    ## huggingface models
    if api_type == 'huggingface':
        # print(cache_dir)
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", use_auth_token=AUTH_TOKEN, cache_dir=cache_dir)
        tokenizer = AutoTokenizer.from_pretrained(model_id, device_map="auto", use_auth_token=AUTH_TOKEN, cache_dir=cache_dir)
        return model, tokenizer
    elif api_type == "vllm":
        model = LLM(model=model_id, max_model_len=35000)
        return model, None
    else:
        return model_id, None      



def main(model_id, dataset, cache_dir, write_dir, with_tests):
    json_path = "../model_config.json"
    model_config = json.load(open(json_path, 'r'))
    api_type = model_config[model_id]["api"]
    root_dir = find_path(dataset)
    if with_tests:
        write_root = os.path.join(write_dir, 'BL', model_id.split("/")[-1], dataset+"-tests")
    else:
        write_root = os.path.join(write_dir, 'BL', model_id.split("/")[-1], dataset)
    if not os.path.exists(write_root):
        os.makedirs(write_root)
    model, tokenizer = load_model(model_id, cache_dir, api_type)
    for d in tqdm(os.listdir(root_dir)):

        write_folder = os.path.join(write_root, d)
        if not os.path.exists(write_folder):
            os.mkdir(write_folder)
        write_path = os.path.join(write_folder, 'response.txt')
        if os.path.exists(write_path):
            continue

        buggy_path = os.path.join(root_dir, d, 'buggy.txt')
        entry_path = os.path.join(root_dir, d, 'entry.txt')
        tests_path = os.path.join(root_dir, d, 'tests.txt')
        nl_path = os.path.join(root_dir, d, 'nl.txt')
        if not os.path.exists(buggy_path):
            continue
        buggy_code = open(buggy_path, 'r').read().strip("\n")
        nl = open(nl_path, 'r').read().strip("\n")
        entry_point = open(entry_path, 'r').read().strip('\n')
        tests = open(tests_path, 'r').read().strip('\n')

        if not with_tests:
            tests = ''
        prompt = create_prompt(model_id, buggy_code, entry_point, tests, nl)
        if api_type=="openai":
            err_flg, response = chatgpt_generator(model_id, prompt)
            if err_flg:
                response = 'ERR: reaches maximum context length'
        if api_type == "huggingface":
            response = huggingface_generator((model, tokenizer), prompt, MAX_NEW_TOKEN)
        if api_type == "huggingface_chat":
            response = huggingface_generator_chat((model, tokenizer), prompt, MAX_NEW_TOKEN)
        if api_type == "litellm":
            response = generator_lllm(model_id, prompt)
        if api_type == "gai":
            response = generator_gemini(model_id, prompt)
        if api_type == "vllm":
            response = generator_vllm(model, prompt)        
        with open(write_path, 'w') as wr:
            wr.write(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [CodeNet, Avatar, cruxeval, mbpp, humaneval]")
    parser.add_argument("--cache", type=str, default="./cache")
    parser.add_argument("--writePath", type=str, default="../Experiment_Results")
    parser.add_argument("--add_tests", action='store_true' )
    args = parser.parse_args()

    model_id = args.model
    dataset = args.dataset
    cache_dir = args.cache
    write_dir = args.writePath
    with_tests = args.add_tests
    main(model_id, dataset, cache_dir, write_dir, with_tests)
    # find_path(dataset, pl)
