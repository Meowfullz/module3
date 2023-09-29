def sort (scores, names, first: int):
	# I wasn't sure how to implement sorting names, so I did it kind of weird
	"""_summary_

	Args:
		data (_type_): _description_
		first (int): _description_
	"""

	#initialize loop counter variable named i
	i = len(scores) - first - 1

	#initialize loop counter variable named j
	j = 0

	# initialize variable named big that will be used
	# to store the index of the biggest value 
	big = 0

	# initialize variable named temp that will be used to
	# swap list values
	temp = 0

	# loop through list as many times as specified by
	# len(data) and first
	# this loop represents the blue arrow
	while (i > 0):
		# set big equal to first
		big = first

		# set j equal to first + 1
		j = first + 1

		# loop through list starting with element at
		# first + 1 and continue until you reach first + i
		# this loop represents the yellow arrow
		while (j <= first + i):
			# if the value in data[big] is less than
			# data[j]
			if (scores[big] < scores[j]):
				#set big equal to j
				big = j
			
			# increment j by 1
			j += 1

		# swap the data in first + i with the data in big 
		# set temp to value in data[first + i]
		temp = scores[first+i]

		#set data[first + i] = data[big]
		scores[first+i] = scores[big]

		#set data[big] to value in temp
		scores[big] = temp

		# decrement i by 1 
		i -= 1
		