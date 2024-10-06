import sys
import trace
from main import incr_list


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('incr_list([5, 2, 5, 2, 3, 3, 9, 0, 123])')
