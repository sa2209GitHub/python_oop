#
#   30
#
# Exception propagation
# ('try', 'except', 'finally', 'else')

def func2():
    return 1 / 0


def func1():
    return func2()


print("When forty winters shall beseige thy brow,")
print("And dig deep trenches in thy beauty's field,")
print("Thy youth's proud livery, so gazed on now,")
print("Will be a tatter'd weed, of small worth held:")

try:
    func1()
except Exception as e:
    print(f"\n>>>>>>>>>>>>> {e} <<<<<<<<<<<<<")

print()
print("Then being ask'd where all thy beauty lies,")
print("Where all the treasure of thy lusty days,")
print("To say, within thine own deep-sunken eyes,")
print("Were an all-eating shame and thriftless praise.")
print("\n. . .\n")
