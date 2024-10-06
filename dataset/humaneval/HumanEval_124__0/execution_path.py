import sys
import trace
from main import valid_date


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("valid_date('01-01-2007')")
