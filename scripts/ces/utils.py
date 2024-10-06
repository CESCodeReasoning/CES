from tree_sitter import Language, Parser
import os
import shutil

Language.build_library(
  'build/my-languages.so',
  ['/home/changshu/tree-sitter-python']  # path to the tree-sitter-pyton repo
)
PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

def run_query(tree, query_text):
    query = PY_LANGUAGE.query(query_text)
    captures = query.captures(tree.root_node)
    return captures
    

def search_loop(tree):
    ## extract loop structure, return {(start_byte, end_byte):"For/While"}
    query= """
[((for_statement)@for_loop)
(while_statement)@while_loop]
    """
    results = {}
    captures = run_query(tree, query)
    for capture in captures:
        label = capture[1]
        byte_start = capture[0].start_byte
        byte_end = capture[0].end_byte
        position = (byte_start, byte_end)
        results[position] = label
    for k in results.copy():
        for j in results.copy():
            if k != j:
                if k[0]>j[0] and k[1] <= j[1]:
                    ## k in a loop inside j
                    results.pop(k)
                    results[j] = 'nested_loop'
                
    return results

def search_condition(tree):
    ## ectract conditional statement
    query = """
[((if_statement)@if)
(elif_clause)@elif
]
"""
    results = {}
    captures = run_query(tree, query)
    for capture in captures:
        label = capture[1]
        byte_start = capture[0].start_byte
        byte_end = capture[0].end_byte
        position = (byte_start, byte_end)
        results[position] = label
    copy_results = results.copy()
    for k in copy_results:
        for j in copy_results:
            if copy_results[k] == 'elif' and k[0]>j[0] and k[1] <= j[1]:
                if k in results:
                    results.pop(k)
                results[j] = 'else_if'
    ## check nested if
    for k in copy_results:
        for j in copy_results:
            if copy_results[k] == 'if' and copy_results[k] =='if' and k[0]>j[0] and k[1] < j[1]:
                if k in results:
                    results.pop(k)
                results[j] = 'nested_if'
                
            
    return results



def parse_file(file_path):
    file = open(file_path, 'r')
    source_code = file.read()
    tree = parser.parse(bytes(source_code, 'utf-8'))
    loops = search_loop(tree)
    conditions = search_condition(tree)
    label = 'if'
    
    ## case 1. no loop, only conditional statement:
    ## Three possibilities: nested_if >else_if > if
    if not loops and conditions:
        # print(conditions)
        label = "if"
        for k in conditions:
            if conditions[k] == "nested_if":
                label = "nested_if"
            elif conditions[k] == "else_if" and label == "if":
                label = "else_if"
        label = [label]
    ## case 2. no conditions, only loops:
    ## Three possibilities: nested loop > for = while
    elif not conditions and loops:
        label = []
        for k in loops:
            if k not in label:
                label.append(loops[k])
    ## case 3. with conditions and loops. 
    elif loops and conditions:
        flags = []
        for i in loops:
            for k in conditions:
                if k[0]>i[0] and k[1]<=i[1]:
                    flag = f"{conditions[k]} in {loops[i]}"
                    if flag not in flags:
                        flags.append(flag)
        if not flags: ## conditions outside loops
           for i in loops:
            for k in conditions:
                flag = f"{conditions[k]} outside {loops[i]}"
                if flag not in flags:
                    flags.append(flag)
        label = flags
    else:
        label = ["simple"]
    return label
        
def parse_all(root):
    labels= []
    for d in os.listdir(root):
        code_path = os.path.join(root, d, 'main.py')
        # print(code_path)
        r = parse_file(code_path)
        for i in r:
            if i == 'nested_loop':
                print(code_path)
            if i not in labels:
                labels.append(i)
    print(labels)


def clean_folder():
    root = "/home/changshu/CodeMind_Results/results/adaptive_loop_condition_branch_condition_only/deepseek-coder-6.7b-instruct/humaneval"
    for d in os.listdir(root):
        sub_root = os.path.join(root, d)
        for j in os.listdir(sub_root):
            if '__' in j:
                folder = os.path.join(sub_root, j)
                shutil.rmtree(folder)
            
if __name__ == "__main__":
    # root = "/home/changshu/CODEMIND/dataset/humaneval"
    # parse_all(root)
    # path = "/home/changshu/CODEMIND/dataset/humaneval/HumanEval_109/main.py"
    # print(parse_file(path))
    clean_folder()
