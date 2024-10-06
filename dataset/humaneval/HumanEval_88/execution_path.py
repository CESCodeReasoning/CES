import sys
import trace
from main import sort_array


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_array([15, 42, 87, 32 ,11, 0])')
