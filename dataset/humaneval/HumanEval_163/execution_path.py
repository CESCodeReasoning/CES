import sys
import trace
from main import generate_integers


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('generate_integers(2, 10)')
