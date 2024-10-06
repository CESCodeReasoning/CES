import sys
import trace
from main import by_length


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('by_length([2, 1, 1, 4, 5, 8, 2, 3])')
