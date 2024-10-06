import sys
import trace
from main import fix_spaces


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('fix_spaces("Example")')
