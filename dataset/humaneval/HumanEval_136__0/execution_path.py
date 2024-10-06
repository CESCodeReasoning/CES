import sys
import trace
from main import largest_smallest_integers


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('largest_smallest_integers([])')
