import sys
import trace
from main import sum_squares


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('sum_squares([0])')
