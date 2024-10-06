import sys
import trace
from main import can_arrange


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('can_arrange([1,2,4,5])')
