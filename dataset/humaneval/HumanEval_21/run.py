from typing import *
def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

output = rescale_to_unit([2.0, 49.9]) 
file = open("/home/changshu/CODEMIND/dataset/humaneval/HumanEval_21/output.txt", 'w')
file.write(str(output))
file.close()
    