import sys
import trace
from main import compare_one


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('compare_one(5, 6)')
