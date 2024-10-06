import sys
import trace
from main import hex_key


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('hex_key("AB")')
