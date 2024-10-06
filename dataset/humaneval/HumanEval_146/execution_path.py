import sys
import trace
from main import specialFilter


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('specialFilter([5, -2, 1, -5])')
