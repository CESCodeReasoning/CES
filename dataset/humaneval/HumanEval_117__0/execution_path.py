import sys
import trace
from main import select_words


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('select_words("Hello world", 4)')
