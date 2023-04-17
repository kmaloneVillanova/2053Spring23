print("Hello World!")

# this is a comment
'this is another way to make a comment'
'''
used to comment what a function or class does
usually comments take up severl lines
'''

# Variables
x = 100
x = 'hello'
x = [1,2,3]

intx = 100
inty = 10
result = intx/inty
print(result)
result = int(result)
print(result)

result = intx // inty
print(result)

# math module
min_val = min(10,2)
print(min_val)
raised = pow(2,4)
print(raised)
raised = 2 ** 4

# if statements
x = -1
y = 1
if x < 0:
    print('x less than 0')

if x < 0 and y > 0:
    print("x and y in range")

if x < 0 or y > 0:
    print("x and y in range")

if x < 0:
    print('x less than 0')
elif x > 0:
    print('x > 0')
else:
    print('x is 0')

print("There's a dog in the yard")
print('He said, "blah blah blah"')

# Loops
counter = 0
while counter < 10:
    print(counter)
    counter += 1

a_list = [10,20,30,40,50]
for i in range(5):
    print(i, a_list[i])

for i in range(2, len(a_list)):
    print(a_list[i])

for i, val in enumerate(a_list):
    print(i, val)

for i in range(len(a_list)-1, -1, -1):
    print(i, a_list[i])

for val in a_list:
    print(val)

def hello_world():
    print("hello world!")

hello_world()

def hello(name="Alice"):
    print("hello", name)
hello("Bob")
hello()

for i in range(len(a_list)):
    print(a_list[i], end=", ")
print()

f_name = 'Kathleen'
l_name = "Malone"
full_name = f_name + " " + l_name
print(full_name)

print(full_name[0])
print(full_name[-1])

print(full_name)
fn=full_name[:8]
print(fn)
ln=full_name[9:]
print(ln)


               







