import sys
import trace
from main import remove_duplicates


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('remove_duplicates([1, 2, 3, 2, 4, 3, 5])')
