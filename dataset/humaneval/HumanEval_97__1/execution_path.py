import sys
import trace
from main import multiply


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('multiply(76, 67)')
