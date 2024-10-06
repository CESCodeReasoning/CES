import sys
import trace
from main import get_max_triples


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_max_triples(6)')
