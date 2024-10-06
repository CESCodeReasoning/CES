import sys
import trace
from main import derivative


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('derivative([3, 2, 1])')
