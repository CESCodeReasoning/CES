import sys
import trace
from main import make_a_pile


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('make_a_pile(3)')
