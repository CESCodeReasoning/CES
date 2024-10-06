import sys
import trace
from main import closest_integer


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('closest_integer("10")')
