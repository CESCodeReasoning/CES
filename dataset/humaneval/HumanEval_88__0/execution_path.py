import sys
import trace
from main import sort_array


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_array([2, 4, 3, 0, 1, 5, 6])')
