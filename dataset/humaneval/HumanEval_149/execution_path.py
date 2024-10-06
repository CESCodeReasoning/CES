import sys
import trace
from main import sorted_list_sum


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sorted_list_sum(["aa", "a", "aaa"])')
