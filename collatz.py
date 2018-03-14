import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--num" , type = int , help="Enter a number")
args = parser.parse_args()
k = args.num
while k != 1:
	if (k % 2) == 0:
		k = k / 2
		print (k)
	else :
		k = 3*k + 1
		print (k)
