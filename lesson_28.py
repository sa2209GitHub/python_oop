#
#   28
#
# Introduction to
# Exception Handling
# 'try' and 'except' Blocks

print("When forty winters shall beseige thy brow,")
print("And dig deep trenches in thy beauty's field,")
print("Thy youth's proud livery, so gazed on now,")
print("Will be a tatter'd weed, of small worth held:")
print()
print("Then being ask'd where all thy beauty lies,")
print("Where all the treasure of thy lusty days,")
print("To say, within thine own deep-sunken eyes,")
print("Were an all-eating shame and thriftless praise.")
print("\n. . .\n")

try:
    print('Shakespire' / 0)
except Exception:
    print("Error")

    print("Regular completion\n")


try:
    file_name = "file.txt"
    f = open(file_name)
except FileNotFoundError:
    print(f"'{file_name}' not found")

print("Regular completion")

try:
    x, y = map(int, input("Enter two numbers separated by a space: ").split())
    result = x / y
except ValueError:
    print('Data type Error')
except ArithmeticError:
    print("Division by zero Error")

print("Regular completion")
