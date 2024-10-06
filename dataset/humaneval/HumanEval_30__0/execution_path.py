import sys
import trace
from main import get_positive


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10])')
