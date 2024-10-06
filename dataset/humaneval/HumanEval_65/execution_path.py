import sys
import trace
from main import circular_shift


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('circular_shift(100, 2)')
