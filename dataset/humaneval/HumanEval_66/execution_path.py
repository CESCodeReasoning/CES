import sys
import trace
from main import digitSum


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('digitSum("You arE Very Smart")')
