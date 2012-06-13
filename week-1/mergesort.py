array = [5,8,1,3,2,4,9,7,10,15,12,13,11,14,16]

def mergeSort(input):
	if len(input) == 1:
		return input	
	else:
		halfPoint = len(input)/2
		firstHalf = mergeSort(input[0:halfPoint])
		secondHalf = mergeSort(input[halfPoint:])
		i = j = 0
		output = []
		
		while len(output) != len(input):
			if i == halfPoint:
				output.append(secondHalf[j])
				j += 1
			elif j == halfPoint:
				output.append(firstHalf[i])
				i += 1
			else:				
				if firstHalf[i] < secondHalf[j]:
					output.append(firstHalf[i])
					i += 1
				elif secondHalf[j] < firstHalf[i]:
					output.append(secondHalf[j])
					j += 1
					
		print output
		return output
		
mergeSort(array)