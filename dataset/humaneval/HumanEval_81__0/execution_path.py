import sys
import trace
from main import numerical_letter_grade


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('numerical_letter_grade([1.2])')
