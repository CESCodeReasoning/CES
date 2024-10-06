import sys
import trace
from main import exchange


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('exchange([100, 200], [200, 200])')
