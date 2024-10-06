import sys
import trace
from main import find_max


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('find_max(["name", "of", "string"])')
