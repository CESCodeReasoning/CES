import sys
import trace
from main import count_nums


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('count_nums([1, 6, 9, -6, 0, 1, 5])')
