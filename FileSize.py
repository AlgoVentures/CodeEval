import os
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  print os.path.getsize(test)

test_cases.close()

