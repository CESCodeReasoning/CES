import sys
import trace
from main import sort_third


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sort_third([1, 2, 3])')
