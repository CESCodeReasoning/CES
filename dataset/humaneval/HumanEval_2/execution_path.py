import sys
import trace
from main import truncate_number


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('truncate_number(3.5)')
