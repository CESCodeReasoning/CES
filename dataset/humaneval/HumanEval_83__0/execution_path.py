import sys
import trace
from main import starts_one_ends


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('starts_one_ends(4)')
