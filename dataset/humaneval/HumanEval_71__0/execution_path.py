import sys
import trace
from main import triangle_area


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('triangle_area(1, 2, 3)')
