import sys
import trace
from main import special_factorial


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('special_factorial(5)')
