import sys
import trace
from main import anti_shuffle


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("anti_shuffle('Hello World!!!')")
