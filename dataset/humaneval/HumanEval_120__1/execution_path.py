import sys
import trace
from main import maximum


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('maximum([123, -123, 20, 0 , 1, 2, -3], 3)')
