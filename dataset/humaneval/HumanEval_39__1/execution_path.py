import sys
import trace
from main import prime_fib


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('prime_fib(4)')
