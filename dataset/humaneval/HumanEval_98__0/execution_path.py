import sys
import trace
from main import count_upper


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("count_upper('dBBE')")
