import sys
import trace
from main import get_odd_collatz


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_odd_collatz(14)')
