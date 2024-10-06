import sys
import trace
from main import how_many_times


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("how_many_times('', 'x')")
