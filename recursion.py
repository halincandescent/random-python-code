def listSum(numList: list[float]) -> float:
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listSum(numList[1:])


def listListSum(numListList: list[int]) -> int:
	count = 0 
	for obj in numListList:
		if type(obj) == int:
			count = count + obj 
		else:
			count = count + listListSum(obj) 	
	return count 		


def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)




## test
print(listSum([2,4,7,5,6,8]) == 32)
print(listListSum([1,2,[3,4],[5,6]]) == 21)
print(factorial(3) == 6)

