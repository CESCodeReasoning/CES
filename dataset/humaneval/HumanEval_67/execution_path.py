import sys
import trace
from main import fruit_distribution


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('fruit_distribution("5 apples and 6 oranges",19)')
