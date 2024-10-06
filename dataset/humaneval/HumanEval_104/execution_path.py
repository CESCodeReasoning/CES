import sys
import trace
from main import unique_digits


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('unique_digits([15, 33, 1422, 1])')
