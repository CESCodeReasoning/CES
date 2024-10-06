import sys
import trace
from main import string_sequence


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('string_sequence(3)')
