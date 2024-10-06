import sys
import trace
from main import count_up_to


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('count_up_to(18)')
