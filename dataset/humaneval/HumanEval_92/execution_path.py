import sys
import trace
from main import any_int


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('any_int(2, 3, 1)')
