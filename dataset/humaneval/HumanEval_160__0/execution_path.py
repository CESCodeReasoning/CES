import sys
import trace
from main import do_algebra


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("do_algebra(['//', '*'], [7, 3, 4])")
