import sys
import trace
from main import reverse_delete


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('reverse_delete("mamma", "mia")')
