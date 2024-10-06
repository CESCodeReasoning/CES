import sys
import trace
from main import max_element


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('max_element([-5, 2, 48, 9, 4, 0, 6, 7])')
