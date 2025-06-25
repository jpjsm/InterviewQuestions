#!/usr/bin/env python3

def IsPalindromic(l):
    half = int(len(l)/2)
    for i in range(0,half + 1):
        if l[i] != l[len(l)-1-i]:
            return False
    return True

class Node(object):
    def __init__(self, value, parent=None, children=[]):
        self.Value = value

        self.Children = []
        
        if children is not None:
            if not isinstance(children, list):
                raise ValueError("'children' must be a list.")

            if len(children) > 0 and not all(isinstance(c, Node) for c in children):
                raise ValueError("All 'children' items must be of Node type.")

            self.Children = children
        
        self.Parent = None
        if parent is not None and not isinstance(parent, Node):
            raise ValueError("'parent' must be of Node type.")

        self.Parent = parent


if (__name__ == "__main__"):
  print("... starting ...")
  for l in [ "abcba", [2,3,5,7,11,13,11,7,5,3,2],"hello",["hello","world","hello"],[0],["hello"]]:
    print("{0} is palindromic: {1}".format(l, IsPalindromic(l)))

  for t in [1, None, [1,2,3]]:
    n0 = Node(t)
    if n0.Value != t:
      print("n0.Value '{0}' != {1}".format(t, n0.Value))
    else:
      print("Success: n0.Value '{0}'".format(n0.Value))

