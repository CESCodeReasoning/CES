import sys
import trace
from main import is_multiply_prime


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('is_multiply_prime(5)')
