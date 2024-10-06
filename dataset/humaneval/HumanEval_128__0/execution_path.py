import sys
import trace
from main import prod_signs


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('prod_signs([-1, 1, 1, 1])')
