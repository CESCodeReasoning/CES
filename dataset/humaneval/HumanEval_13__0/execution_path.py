import sys
import trace
from main import greatest_common_divisor


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('greatest_common_divisor(10, 15)')
