import sys
import trace
from main import below_zero


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('below_zero([1, -1, 2, -2, 5, -5, 4, -4])')
