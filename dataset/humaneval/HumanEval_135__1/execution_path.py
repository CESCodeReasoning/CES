import sys
import trace
from main import can_arrange


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('can_arrange([4,8,5,7,3])')
