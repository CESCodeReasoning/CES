import sys
import trace
from main import skjkasdkd


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('skjkasdkd([0,8,1,2,1,7])')
