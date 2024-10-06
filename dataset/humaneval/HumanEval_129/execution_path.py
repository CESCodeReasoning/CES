import sys
import trace
from main import minPath


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)')
