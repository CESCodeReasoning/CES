import sys
import trace
from main import is_equal_to_sum_even


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('is_equal_to_sum_even(4)')
