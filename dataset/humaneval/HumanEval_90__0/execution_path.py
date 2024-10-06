import sys
import trace
from main import next_smallest


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('next_smallest([5, 1, 4, 3, 2])')
