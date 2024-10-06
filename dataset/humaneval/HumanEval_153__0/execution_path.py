import sys
import trace
from main import Strongest_Extension


tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=0)
tracer.run("Strongest_Extension('Sp', ['671235', 'Bb'])")
