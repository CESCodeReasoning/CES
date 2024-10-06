import sys
import trace
from main import intersection


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('intersection([-1, 1], [0, 4])')
