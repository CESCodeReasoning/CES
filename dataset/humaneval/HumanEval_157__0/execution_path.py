import sys
import trace
from main import right_angle_triangle


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('right_angle_triangle(7, 24, 25)')
