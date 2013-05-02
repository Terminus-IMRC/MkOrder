#!/usr/bin/env python
import sys

X=0

def MkOrder(ar, level):
	if level==X:
		for i in ar:
			print "%d " %(i),
		print
	else:
		for i in range(len(ar)):
			if not((i==0 and level==X-1) or (i==X-1 and level==0)):
				if ar[i] == X:
					ar[i]=level
					MkOrder(ar, level+1)
					ar[i]=X

if __name__ == '__main__':
	if len(sys.argv)!=2:
		print >>sys.stderr, "Invalid The argument."
		exit(1)
	X=int(sys.argv[1])
	ar=[X]*X
	MkOrder(ar, 0)
