import sys
import trace
from main import rolling_max


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('rolling_max([1, 2, 3, 4])')
