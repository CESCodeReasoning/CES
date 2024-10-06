import os
import json
def cleanup(result_root):
    for d in os.listdir(result_root):
        path_fix = os.path.join(result_root, d, 'response_0.txt')
        path_bug = os.path.join(result_root, d, 'response_1.txt')
        
        for f in [path_fix, path_bug]:
            text = open(f, 'r').read()
            if "Magicoder" in result_root:
                response = text.split("Code:")[2].split("```response")[-1].split("```")[0].strip().strip("\n")
            elif "semcoder" in result_root:
                response = text.split("Response:")[-1].split("```response")[-1].split("```")[0].strip().strip("\n")
            else:
                response = text.split("```response")[1].split("```")[0].strip().strip("\n")
            wr_path = f.replace("response", "predict")
            with open(wr_path, 'w') as wr:
                wr.write(response)

def check_output(result_root):
    model_name = result_root.split("/")[-2]
    wr_path = f"/home/changshu/CODEMIND/Experiment_Results/BP/summary/{model_name}.json"
    results = {}
    correct, total = 0,0
    for d in os.listdir(result_root):
        total += 1
        path_fix = os.path.join(result_root, d, 'predict_0.txt')
        path_bug = os.path.join(result_root, d, 'predict_1.txt')
        
        pred_fix = open(path_fix, 'r').read()
        pred_buggy = open(path_bug, 'r').read()
        if "No" in pred_fix:
            # correct += 1
            pass
        if "Yes" in pred_buggy:
            correct += 1
            results[d] = 1
        else:
            results[d] = 0
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)
    print(correct, total, correct/total)

check_output("/home/changshu/CODEMIND/Experiment_Results/BP/starcoder2-15b/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/Magicoder-S-DS-6.7B/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/gpt-4-turbo/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/deepseek-coder-33b-instruct/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/CodeLlama-34b-Instruct-hf/HumanEvalFix-tests")
# cleanup("/home/changshu/CODEMIND/Experiment_Results/BP/gemini-1.5-pro/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/gemini-1.5-pro/HumanEvalFix-tests")

# cleanup("/home/changshu/CODEMIND/Experiment_Results/BP/semcoder_s/HumanEvalFix-tests")
# check_output("/home/changshu/CODEMIND/Experiment_Results/BP/semcoder_s/HumanEvalFix-tests")