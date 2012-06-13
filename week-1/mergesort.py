array = [5,8,1,3,2,4,9,7,10,15,12,13,11,14,6]

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
			if firstHalf[i] < secondHalf[j]:
				output.append(firstHalf[i])
				i += 1
			elif secondHalf[j] < firstHalf[i]:
				output.append(secondHalf[j])
				j += 1
				
			if i == len(firstHalf) or j == len(secondHalf):
				output.extend(secondHalf[j:] or firstHalf[i:])
					
		print output
		return output
		
mergeSort(array)