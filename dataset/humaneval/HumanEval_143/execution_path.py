import sys
import trace
from main import words_in_sentence


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('words_in_sentence("This is a test")')
