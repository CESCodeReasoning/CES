import sys
import trace
from main import maximum


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('maximum([-3, 2, 1, 2, -1, -2, 1], 1)')
