import sys
import trace
from main import remove_vowels


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("remove_vowels('fedcba')")
