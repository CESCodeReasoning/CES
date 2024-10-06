import sys
import trace
from main import correct_bracketing


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('correct_bracketing("<<<><>>>>")')
