import sys
import trace
from main import pluck


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('pluck([5, 0, 3, 0, 4, 2])')
