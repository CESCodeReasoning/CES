import sys
import trace
from main import add_elements


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('add_elements([1,-2,-3,41,57,76,87,88,99], 3)')
