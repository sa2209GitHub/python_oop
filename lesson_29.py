# Exception Handling.
# 'finally' and 'else' Blocks

try:
    x, y = map(int, input("Enter two numbers separated by a space: ").split())
    result = x / y
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("try block didn't throw any exception")
finally:
    print("the finally block is executed anyway")


try:
    # f = open("./myfile.txt", "a")
    f = open("./myfile.txt", "w")
    # f = open("./myfile.txt")
    f.write("Lesson 29. Exception Handling. 'finally' and 'else' Blocks\n")
except FileNotFoundError as err:
    print(err)
except:
    print("Unknown Exception Error")
finally:
    if f:
        f.close()
        print("The file has been closed")


try:
    with open("./myfile.txt", "a") as f:
        f.write(
            "Lesson 29(2). Exception Handling. 'finally' and 'else' Blocks...\nSee you in lesson 32 . . .\n")
except FileNotFoundError as err:
    print(err)
except:
    print("Unknown Exception Error")


def get_values():
    try:
        x, y = map(int, input(
            "Enter two numbers separated by a space: ").split())
        return x, y
    except ValueError as e:
        print(e)
        return 0, 0
    finally:
        print("The 'finally' block is executed before the 'return' statement")


x, y = get_values()
print(x, y)


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return e


def get_values2():
    try:
        x, y = map(int, input(
            "Enter two numbers separated by a space: ").split())
        result = div(x, y)
        return result
    except ValueError as e:
        print(e)


result = get_values2()
print(result)
