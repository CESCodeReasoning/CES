import sys
import trace
from main import parse_nested_parens


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("parse_nested_parens('(()(())((())))')")
