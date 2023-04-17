value = input()
print('you entered',value)

num = int(input("Enter a number"))
print('you entered',num)
num += 1

with open('movies.txt') as file:
    for line in file:
        line=line.strip()
        print(line)

with open('heights.txt') as file:
    for line in file:
        line=line.strip()
        values=line.split()
        print(values)
        fname=values[0]
        lname=values[1]
        height=int(values[2])
        print(height)


