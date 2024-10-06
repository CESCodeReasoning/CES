import sys
import trace
from main import even_odd_count


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('even_odd_count(-78)')
