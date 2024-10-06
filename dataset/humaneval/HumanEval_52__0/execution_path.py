import sys
import trace
from main import below_threshold


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('below_threshold([1, 8, 4, 10], 11)')
