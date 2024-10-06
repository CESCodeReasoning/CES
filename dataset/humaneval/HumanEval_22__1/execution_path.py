import sys
import trace
from main import filter_integers


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("filter_integers([4, {}, [], 23.2, 9, 'adasd'])")
