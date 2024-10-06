import sys
import trace
from main import has_close_elements


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95)')
