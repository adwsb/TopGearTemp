def isListOfInts(inp):
	
	if not isinstance(inp, list):
		raise Exception("ValueError - arg not of <list> type")

	res = True
	
	for x in inp:
		if isinstance(x, int):
			res = res and True
		else:
			res = res and False

	return res


def testList(inp):
	try:
		print(isListOfInts(inp))
	except Exception as e:
		print(e)





testList([])
testList([1])
testList([1,2])
testList([0])
testList(['1'])
testList([1,'a'])
testList(['a',1])
testList([1, 1.])
testList([1., 1.])
testList((1,2))
