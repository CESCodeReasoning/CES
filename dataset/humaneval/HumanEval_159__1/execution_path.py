import sys
import trace
from main import eat


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('eat(2, 11, 5)')
