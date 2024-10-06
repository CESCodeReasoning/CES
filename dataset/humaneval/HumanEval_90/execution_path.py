import sys
import trace
from main import next_smallest


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('next_smallest([1, 2, 3, 4, 5])')
