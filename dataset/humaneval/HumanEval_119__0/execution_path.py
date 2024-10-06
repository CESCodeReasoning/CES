import sys
import trace
from main import match_parens


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("match_parens(['())(', '()'])")
