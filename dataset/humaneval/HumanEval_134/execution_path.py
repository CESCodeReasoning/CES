import sys
import trace
from main import check_if_last_char_is_a_letter


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run('check_if_last_char_is_a_letter("apple")')
