import sys
import trace
from main import rescale_to_unit


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])')
