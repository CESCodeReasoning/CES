import sys
import trace
from main import choose_num


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('choose_num(12, 15)')
