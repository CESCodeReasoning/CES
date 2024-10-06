import sys
import trace
from main import sum_product


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sum_product([1,1,1])')
