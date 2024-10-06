import os
import subprocess
from tqdm import tqdm
import json

def cleanup(result_root):
    root_dataset = "../dataset/Intermediate/Repair/HumanEvalFix"
    for d in os.listdir(result_root):
        response_path = os.path.join(result_root, d, 'response.txt')
        tests_path = os.path.join(root_dataset, d, 'tests.txt')
        ut_path = os.path.join(result_root, d, 'ut.py')
        response = open(response_path, 'r').read()
        if 'starcoder' in response_path:
            fixed_code = response.split("<fim_suffix><fim_middle>")[-1].split('```python')[1].split("```")[0]
        elif 'semcoder' in response_path:
            try:
                fixed_code = response.split("Buggy Code:")[2].split('```python')[1].split("```")[0]
            except:
                fixed_code = "NA"
                print(d)
        # elif 'deepseek' in response_path:
        #     fixed_code = response.split("<fim_suffix><fim_middle>")[-1].split('```python')[1].split("```")[0]
        else:
            if 'CodeLlama' in response_path or 'Mistral' in response_path:
                fixed_code = response.split('[/INST]')[-1]
                try:
                    if '```python' in fixed_code:
                        fixed_code = fixed_code.split('```python')[-1].split("```")[0]
                    else:
                        fixed_code = fixed_code.split('```')[1]
                except:
                    print(response_path)
            else:
                fixed_code = response.split('```python')[-1].split("```")[0]
            if 'def check(' in fixed_code:
                fixed_code = fixed_code.split('def check(')[0]
        test_cases = open(tests_path, 'r').read()
        code_ut = fixed_code +  '\n' + test_cases
        with open(ut_path, 'w', encoding='utf-8') as f:
            f.write(code_ut)

def test_python(py_path):
    test_result_flag = 1 ## pass
    try:
        test_result = subprocess.run(
        ['python', py_path],
        capture_output = True,
        text = True,
        timeout=100
        )
        
        if test_result.stderr:
            test_result_flag = 0
    except:
        test_result_flag = 0
    return test_result_flag

def test_code(result_root):
    model_name = result_root.split("/")[-2]
    wr_path = f"/home/changshu/CODEMIND/Experiment_Results/APR/summary/{model_name}.json"
    results = {}
    pass_count, total_count = 0, 0
    for d in tqdm(os.listdir(result_root)):
        total_count += 1
        path_ut = os.path.join(result_root, d, 'ut.py')
        status = test_python(path_ut)
        if status:
            pass_count += 1
            results[d] = 1
        else:
            results[d] = 0
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)
    print(pass_count, total_count, pass_count/total_count)


result_root = "/home/changshu/CODEMIND/Experiment_Results/APR/semcoder_s/HumanEvalFix-tests"
cleanup(result_root)
test_code(result_root)