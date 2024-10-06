import sys
import trace
from main import int_to_mini_roman


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('int_to_mini_roman(900)')
