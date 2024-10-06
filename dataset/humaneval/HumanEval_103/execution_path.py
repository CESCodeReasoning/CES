import sys
import trace
from main import rounded_avg


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('rounded_avg(1, 5)')
