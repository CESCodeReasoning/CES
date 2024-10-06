import sys
import trace
from main import car_race_collision


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('car_race_collision(4)')
