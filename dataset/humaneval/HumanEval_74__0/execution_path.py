import sys
import trace
from main import total_match


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("total_match(['4'], ['1', '2', '3', '4', '5'])")
