"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: assign
"""

import sys

def main():
  for line in sys.stdin:
    if line.strip() =="#":
        break
    src, dest = line.strip().split()
    w, h = len(src), len(dest);
    print(w,h)
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    print(Matrix)
    for i in range(h):
        for j in range(w):
            down=0
            right=0
            if i > 0:
                down=Matrix[j][i-1]
            if j > 0:
                right=Matrix[j-1][i]
            if down>right:
                v=down
            else:
                v=right
            #print(v)
            if src[i]==dest[j]:
                Matrix[j][i]=v+1
            else:
                Matrix[j][i]=v
            print(Matrix[j][i])
             
    print(Matrix)
if __name__ == '__main__':
  main()
