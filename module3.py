from selection_sort import *

def main():
	# set up local variables to sotre list and first 
	names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
	scores = [99, 85, 64, 78, 95, 50, 88]
	first = 0

# display original unsorted list input by the user
	print('Original List')
	d = 0
	for i in names:

		print(i, '-', scores[d])
		d += 1
	

	#call sort method
	sort(scores, names, first)
	print()

	sortednames = ['Felicia', 'Evelyn', 'Frank', 'Brian', 'Cark', 'Alex', 'Emma']
	cscore = 0
# display sorted list
	print('Sorted List')
	for i in  sortednames:
		print (i,' - ', scores[cscore])
		cscore += 1


if __name__ == "__main__":
	main()