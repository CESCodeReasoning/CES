import sys
import trace
from main import simplify


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('simplify("5/1", "3/1")')
