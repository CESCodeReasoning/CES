import sys
import trace
from main import string_xor


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("string_xor('1', '1')")
