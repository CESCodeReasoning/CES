import sys
import trace
from main import longest


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc'])")
