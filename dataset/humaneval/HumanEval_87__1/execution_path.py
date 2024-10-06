import sys
import trace
from main import get_row


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('get_row([[], [1], [1, 2, 3]], 3)')
