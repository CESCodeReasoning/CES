import sys
import trace
from main import monotonic


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('monotonic([1, 2, 4, 20])')
