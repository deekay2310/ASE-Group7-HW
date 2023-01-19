from misc import *
import sys
from test_engine import test


help = """   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
  -g  the	show settings
  -g  rand	generate, reset, regenerate same
  -g  sym	check syms
  -g  num	check nums
"""

the = cli(sys.argv[1:])

test(the)
if the['help']:
    exit (print("\n" + str(help) + "\n"))


