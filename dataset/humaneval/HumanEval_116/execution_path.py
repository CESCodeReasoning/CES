import sys
import trace
from main import sort_array


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_array([1,5,2,3,4])')
