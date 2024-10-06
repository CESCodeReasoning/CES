import sys
import trace
from main import sort_third


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])')
