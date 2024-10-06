import sys
import trace
from main import smallest_change


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('smallest_change([1,2,3,5,4,7,9,6])')
