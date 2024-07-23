msg = "Roll the dice"
print(msg)

msg = "Role something else"

print(msg)

spam = 12

#Comment

floatResult = 16 / 4
print(floatResult)

integerResult = 16 // 4
print(integerResult)

powerOfResult = 5 ** 2
print(powerOfResult)

threeNames = 3 * "Luka "
print(threeNames)

veryLongString = "123456789"
firstNumber = veryLongString[0]
lastNumber = veryLongString[-1]
firstFiveNumbers = veryLongString[0:5]
lastThreeNumbers = veryLongString[-3:]

#String are immutable, create a new one if you want to change it

print(firstNumber)
print(lastNumber)
print(firstFiveNumbers)
print(lastThreeNumbers)

numberList = [1, 2, 3, 4, 5, 6, 7, 8] + [9, 10, 11]
print(numberList)

#Does not copy values
numberListCopy = numberList
numberListCopy.append(12)
print(numberList)

#How to do a shallow copy
numberListShallowCopy = numberList[:]
numberListShallowCopy.append(13)
print(numberList)

#Assignments to slices are possible
numberListShallowCopy[1:4] = [99, 98, 97]
print(numberListShallowCopy)
