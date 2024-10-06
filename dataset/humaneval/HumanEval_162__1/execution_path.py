import sys
import trace
from main import string_to_md5


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("string_to_md5('A B C')")
