import sys
import trace
from main import odd_count


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("odd_count(['3','11111111'])")
