import sys
import trace
from main import sort_third


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])')
