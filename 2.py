s = "75,41,14,8,73,45,-16"
evenNumbers = []

for number in s.split(","):
    if int(number) % 2 == 0 and int(number) > 0:
        evenNumbers.append(number)

print("Even Numbers : \"{}\"".format(evenNumbers))