"""
Files
"""

# 1.
name = input("Name: ")
outfile = open("name.txt", 'w')
print(name, file=outfile)
outfile.close()

# 2.
infile = open("name.txt", 'r')
name = infile.read()
print(f"Hi {name}")
infile.close()

# 3.
with open("numbers.txt") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)

with open("numbers.txt") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
