import sys
import trace
from main import common


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])')
