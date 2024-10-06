import sys
import trace
from main import add_elements


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('add_elements([11,21,3,90,5,6,7,8,9], 4)')
