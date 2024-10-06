import sys
import trace
from main import max_element


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('max_element([1, 2, 3])')
