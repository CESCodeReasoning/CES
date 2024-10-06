import sys
import trace
from main import words_string


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('words_string("One, two, three, four, five, six")')
