
DebugMode = False
CacheEnabled = False
ParenthesesGroups = {}


def GenerateParenthesesGroups(n):
  if CacheEnabled and n in ParenthesesGroups:
    return ParenthesesGroups[n]

  if n == 0:
    return [""]

  result = []
  for i in range(0,n):
    for l in GenerateParenthesesGroups(i):
      for r in GenerateParenthesesGroups(n - 1 - i):
        s = '(' + l + ')' + r
        result.append(s)

  if CacheEnabled: 
    ParenthesesGroups[n] = result

  return result


if (__name__ == "__main__"):
  print("... starting ...")

  groups = 12
  from datetime import timedelta, datetime  
  
  CacheEnabled = False

  start = datetime.now()
  L = GenerateParenthesesGroups(groups)
  elapsed1 = datetime.now() - start

  CacheEnabled = True


  start = datetime.now()
  L = GenerateParenthesesGroups(groups)
  elapsed2 = datetime.now() - start

  start = datetime.now()
  L = GenerateParenthesesGroups(groups)
  elapsed3 = datetime.now() - start

  print("Generate parenteses ({1}), no cache: {0} milliseconds".format(elapsed1 / timedelta(microseconds=1000), groups))
  print("Generate parenteses ({1}), with cache enabled: {0} milliseconds".format(elapsed2 / timedelta(microseconds=1000), groups))
  print("Generate parenteses ({1}), with cache pre-warmed: {0} milliseconds".format(elapsed3 / timedelta(microseconds=1000), groups))

  for i in range(1,5):
    print("{0}".format(i))
    print(" ",end='')
    for r in GenerateParenthesesGroups(i):
      print("{0}".format(r), end=', ')
    print("")