numbers_file = open("numbers.txt", "r")
lines = numbers_file.read().split(',')
return (int(t[0]), int(t[1]), int(t[2]), t[3])
print(lines)




