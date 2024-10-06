import sys
import trace
from main import fizz_buzz


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('fizz_buzz(50)')
