for repeat in range(1,6):
	for printSpace in range(6-repeat):
		print(" ",end='')
	for printStar in range(repeat*2-1):
		print('*',end='')
	print()