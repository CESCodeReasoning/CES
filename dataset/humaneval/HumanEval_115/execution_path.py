import sys
import trace
from main import max_fill


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)')
