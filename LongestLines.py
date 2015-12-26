

#read in file, split to list
content = [i.rstrip() for i in test_cases]
test_cases = open(sys.argv[1], 'r')

#pop off first value as a number
num = content.pop(0)
num = str(num[0])
#sort remaining list by length
final = content.sort(key = len, reverse=True)
#print first values as indicated by num
for sentance in content[:int(num)]:
    print(sentance)


#print(final)
