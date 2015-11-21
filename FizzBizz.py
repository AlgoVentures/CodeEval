import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  row = [int(x) for x in test.split()]
  
  x = row[0]
  y = row[1]
  n = row[2]
  
  nums = list(range(1,n+1))
  final = []
  for num in nums:
      if num % x == 0 and num % y == 0:
        final.append("FB")
  
      elif num % x == 0:
        final.append("F")
  
      elif num % y == 0:
        final.append("B")
  
      else:
          final.append(str(num))
  print ' '.join(final)




test_cases.close()
