import sys
import trace
from main import find_closest_elements


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1])')
