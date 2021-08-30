height = 1.5
aw = 30; bw = 50; cw = 70

bmi = lambda h, w: w/h**2

if bmi(height, aw) > bmi(height, cw):
	print("A比C重")
else:
	print("A比C輕")

if bmi(height, bw) < 25:
	print("過輕")
elif bmi(height, bw) == 25:
	print("標準")
else:
	print("過重")