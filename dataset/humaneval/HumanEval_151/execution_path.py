import sys
import trace
from main import double_the_difference


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('double_the_difference([0.2, 3, 5])')
