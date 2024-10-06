import sys
import trace
from main import count_distinct_characters


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("count_distinct_characters('aaaaAAAAaaaa')")
