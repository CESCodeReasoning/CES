import sys
import trace
from main import get_positive


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_positive([-1, -2])')
