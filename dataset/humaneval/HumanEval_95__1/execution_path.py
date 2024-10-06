import sys
import trace
from main import check_dict_case


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})')
