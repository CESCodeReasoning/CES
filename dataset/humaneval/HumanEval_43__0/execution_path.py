import sys
import trace
from main import pairs_sum_to_zero


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('pairs_sum_to_zero([-3, 9, -1, 4, 2, 30])')
