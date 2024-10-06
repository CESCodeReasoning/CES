import sys
import trace
from main import move_one_ball


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('move_one_ball([4, 3, 1, 2])')
