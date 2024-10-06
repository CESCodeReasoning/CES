import sys
import trace
from main import cycpattern_check


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('cycpattern_check("winemtt","tinem")')
