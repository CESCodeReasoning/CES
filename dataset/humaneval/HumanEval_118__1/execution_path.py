import sys
import trace
from main import get_closest_vowel


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_closest_vowel("ba")')
