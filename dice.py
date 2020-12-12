def incrementDice(diceList, digit):
	diceList[digit] += 1
	if diceList[digit] == 7:
		diceList[digit] = 1
		incrementDice(diceList, digit-1)

def mostCommonNumber(dice):
	diceList = []
	rollCount = {}
	total = 0

	for i in range(dice):
		diceList.append(1)
	while total != (dice*6):
		total = 0
		for i in diceList:	
			total += i
		if total in rollCount:
			rollCount[total] += 1
		else:
			rollCount[total] = 1
		incrementDice(diceList, len(diceList) - 1)
	return rollCount

def main(start, stop):
	for i in range(start,stop+1):
		print("For " + str(i) + " dice. The most likely number is " + str(mostCommonNumber(i)))

print(mostCommonNumber(7))
