import sys
import trace
from main import compare


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('compare([1,2,3,4,5,1],[1,2,3,4,2,-2])')
