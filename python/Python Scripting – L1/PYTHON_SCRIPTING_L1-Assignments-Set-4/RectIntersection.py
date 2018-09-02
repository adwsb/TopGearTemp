import sys
#format: ((TopLeftX, TopLeftY), (BottomRightX, (BottomRightY))

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]

def intersection(A,B):
	rectangle1 = ((A[0][0],A[0][1]), (A[0][0],A[1][1]), (A[1][0],A[1][1]), (A[1][0],A[0][1]))
	lines1 = (rectangle1[0],rectangle1[1]), (rectangle1[1],rectangle1[2]), (rectangle1[2],rectangle1[3]), (rectangle1[0],rectangle1[3])
	rectangle2 = ((B[0][0],B[0][1]), (B[0][0],B[1][1]), (B[1][0],B[1][1]), (B[1][0],B[0][1]))
	lines2 = (rectangle2[0],rectangle2[1]), (rectangle2[1],rectangle2[2]), (rectangle2[2],rectangle2[3]), (rectangle2[0],rectangle2[3])

	extendedIntersect = []

	for i in lines1:
		for j in lines2:
			try:
				extendedIntersect.append(line_intersection(i,j))
			except:
				continue

	# print(extendedIntersect)
	intersect = []

	for i in extendedIntersect:
		if (i[0] >= A[0][0] and i[0] <= A[1][0] and
			i[1] >= A[0][1] and i[1] <= A[1][1] and
			i[0] >= B[0][0] and i[0] <= B[1][0] and
			i[1] >= B[0][1] and i[1] <= B[1][1] 

		):
			intersect.append(i)


	return intersect
	


A = (((int(sys.argv[1])),int(sys.argv[2])),(int(sys.argv[3]),int(sys.argv[4])))
B = (((int(sys.argv[5])),int(sys.argv[6])),(int(sys.argv[7]),int(sys.argv[8])))

intersectionPoints = intersection(A,B)
# print(intersectionPoints)

try:
	if intersectionPoints[0][0] < intersectionPoints[1][0]:
		ans = intersectionPoints
	else:
		temp = intersectionPoints[0]
		intersectionPoints[0] = intersectionPoints[1]
		intersectionPoints[1] = temp
		ans = intersectionPoints

		# if intersectionPoints[0][1] < intersectionPoints[1][1]:
		# 	ans = [[intersectionPoints[0][0],intersectionPoints[1][1]], [intersectionPoints[1][0],intersectionPoints[0][1]]]

	ans = tuple(tuple(x) for x in ans)
	print(ans[0], ans[1])
except:
	print("Except at Arrange")