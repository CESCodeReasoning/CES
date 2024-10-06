import sys
import trace
from main import flip_case


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("flip_case('These violent delights have violent ends')")
