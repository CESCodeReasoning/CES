import sys
import trace
from main import strange_sort_list


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('strange_sort_list([1, 2, 3, 4])')
