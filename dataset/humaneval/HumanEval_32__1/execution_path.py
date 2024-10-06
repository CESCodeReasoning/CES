import sys
import trace
from main import find_zero


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('find_zero([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])')
