import sys
import trace
from main import mean_absolute_deviation


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('mean_absolute_deviation([1.0, 2.0, 3.0])')
