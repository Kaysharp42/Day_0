import sys

print(f"Input : {sys.argv[1]}")

if len(sys.argv) > 2:
    raise AssertionError("More than one argument given")
x = int(sys.argv[1])
print(type(x))
if type(x) != int:
    raise AssertionError("First argument given is not an integer")

if x % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")