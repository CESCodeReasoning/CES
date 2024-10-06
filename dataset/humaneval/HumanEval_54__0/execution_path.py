import sys
import trace
from main import same_chars


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("same_chars('abcd', 'dddddddabcf')")
