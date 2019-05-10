file = open("174 - Gozáos en el Señor ().xml", "r+", encoding="utf-16")

lines = file.read().split('\n')
for line in lines:
	print(line.find("<verse"))