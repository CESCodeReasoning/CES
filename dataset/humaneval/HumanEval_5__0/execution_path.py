import sys
import trace
from main import intersperse


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('intersperse([5, 6, 3, 2], 8)')
