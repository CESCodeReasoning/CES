import sys
import trace
from main import filter_by_prefix


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("filter_by_prefix(['a', 'ab', 'abc', 'ba', 'bb', 'bc'], 'a')")
