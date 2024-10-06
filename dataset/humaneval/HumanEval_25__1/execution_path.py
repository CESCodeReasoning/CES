import sys
import trace
from main import factorize


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('factorize(3 * 19 * 3 * 19)')
