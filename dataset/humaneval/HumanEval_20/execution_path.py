import sys
import trace
from main import find_closest_elements


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])')
