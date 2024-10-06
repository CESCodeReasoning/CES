import sys
import trace
from main import change_base


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('change_base(8, 3)')
