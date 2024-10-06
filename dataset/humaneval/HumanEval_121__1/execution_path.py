import sys
import trace
from main import solution


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('solution([30, 13, 23, 32])')
