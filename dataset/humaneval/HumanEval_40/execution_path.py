import sys
import trace
from main import triples_sum_to_zero


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('triples_sum_to_zero([1, 3, 5, 0])')
