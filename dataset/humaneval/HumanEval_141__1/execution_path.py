import sys
import trace
from main import file_name_check


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("file_name_check('@this1_is6_valid.exe')")
