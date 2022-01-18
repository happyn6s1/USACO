"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: assign
"""

import sys

def main():
  n=0
  for line in sys.stdin:
    x=''
    for i in range(len(line)):
        if line[i]=='"':
            if n%2 == 0:
                x=x+"``"
            else:
                x=x+"''"
            n=n+1
        else:
            x=x+line[i]
    print(x, end="")
    #print("\n")
  return
if __name__ == '__main__':
  main()
  
