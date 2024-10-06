import sys
import trace
from main import median


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('median([3, 1, 2, 4, 5])')
