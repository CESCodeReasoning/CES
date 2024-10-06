import sys
import trace
from main import order_by_points


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('order_by_points([])')
