import sys
import trace
from main import decimal_to_binary


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('decimal_to_binary(32)')
