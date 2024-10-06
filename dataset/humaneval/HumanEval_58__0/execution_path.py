import sys
import trace
from main import common


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('common([4, 3, 2, 8], [3, 2, 4])')
