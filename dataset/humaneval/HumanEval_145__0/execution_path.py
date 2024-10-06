import sys
import trace
from main import order_by_points


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('order_by_points([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46])')
