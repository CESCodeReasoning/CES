import sys
import trace
from main import unique


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("unique(['a', 'b', 'b', 'c', 'd', 'd'])")
