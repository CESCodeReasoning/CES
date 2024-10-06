import sys
import trace
from main import bf


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('bf("Earth", "Earth")')
