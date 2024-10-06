import sys
import trace
from main import will_it_fly


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('will_it_fly([1, 2, 3], 6)')
