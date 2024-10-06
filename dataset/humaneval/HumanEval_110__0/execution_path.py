import sys
import trace
from main import exchange


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1])')
