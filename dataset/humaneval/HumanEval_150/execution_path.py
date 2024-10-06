import sys
import trace
from main import x_or_y


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('x_or_y(7, 34, 12)')
