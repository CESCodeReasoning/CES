import sys
import trace
from main import filter_integers


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("filter_integers([3, 'c', 3, 3, 'a', 'b'])")
