import sys
import trace
from main import is_bored


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('is_bored("Hello world")')
