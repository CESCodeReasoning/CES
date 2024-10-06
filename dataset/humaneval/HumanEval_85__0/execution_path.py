import sys
import trace
from main import add


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('add([4, 0, 6, 7])')
