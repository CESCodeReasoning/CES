import os
import json
def cleanup(result_root):
    for d in os.listdir(result_root):
        path_bl = os.path.join(result_root, d, 'response.txt')
        if not os.path.exists(path_bl):
            continue
        text = open(path_bl, 'r').read()
        if "Magicoder" in result_root:
            response = text.split("Response:")[-1].split("```response")[-1].split("```")[0].strip().strip("\n")
        elif "semcoder" in result_root:
            response = text.split("Buggy Code:")[2].split("```response")[-1].split("```")[0].strip().strip("\n")
        else:
            response = text.split("```response")[1].split("```")[0].strip().strip("\n")
        wr_path = path_bl.replace("response", "predict")
        with open(wr_path, 'w') as wr:
            wr.write(response)

def check_output(result_root):
    model_name = result_root.split("/")[-2]
    wr_path = f"/home/changshu/CODEMIND/Experiment_Results/BL/summary/{model_name}.json"
    results = {}
    dataset_root = "/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix"
    correct, total = 0,0
    for d in os.listdir(result_root):
        total += 1
        path_bl = os.path.join(result_root, d, 'predict.txt')
        path_gt = os.path.join(dataset_root, d, 'buggy_line.txt')
        pred = open(path_bl, 'r').read().strip('\n').strip()
        gt = open(path_gt, 'r').read().strip('\n').strip()
        if pred == gt:
            correct += 1
            results[d] = 1
        else:
            results[d] = 0
    print(correct, total, correct/total)
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)        
        

# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/starcoder2-15b/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/Magicoder-S-DS-6.7B/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/gpt-4-turbo/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/deepseek-coder-33b-instruct/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/CodeLlama-34b-Instruct-hf/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/gemini-1.5-pro/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/CodeLlama-34b-Instruct-hf/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/deepseek-coder-33b-instruct/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/starcoder2-15b/HumanEvalFix-tests")

# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/gemini-1.5-pro/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/gpt-4-turbo/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/Magicoder-S-DS-6.7B/HumanEvalFix-tests")

# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/CodeLlama-34b-Instruct-hf/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/deepseek-coder-33b-instruct/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BL/starcoder2-15b/HumanEvalFix-tests")   

# cleanup("/home/changshu/CODEMIND/Experiment_Results/BL/semcoder_s/HumanEvalFix-tests")
check_output("/home/changshu/CODEMIND/Experiment_Results/BL/semcoder_s/HumanEvalFix-tests")