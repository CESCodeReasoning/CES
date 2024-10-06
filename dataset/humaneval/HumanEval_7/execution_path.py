import sys
import trace
from main import filter_by_substring


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("filter_by_substring([], 'john')")
