import sys
import trace
from main import unique


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('unique([2, 1, 1, 2, 1, 1])')
