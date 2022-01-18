"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: assign
"""

import sys

def main():
  n=0
  lines=sys.stdin.readlines()
  #lines=["2\n","100 90 130\n","1 3 2\n"]
  n=int(lines[0])
  for i in range(n):
    l=lines[i+1].split()
    l[0]=int(l[0])
    l[1]=int(l[1])
    l[2]=int(l[2])
    l.sort()
    print("Case "+str(i+1)+str(l[1]),end="")
  return
if __name__ == '__main__':
  main()
  
