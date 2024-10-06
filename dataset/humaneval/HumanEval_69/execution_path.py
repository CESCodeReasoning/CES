import sys
import trace
from main import search


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('search([5, 5, 5, 5, 1])')
