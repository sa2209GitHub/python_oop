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
        f.write("Lesson 29(2). Exception Handling. 'finally' and 'else' Blocks\n")
except FileNotFoundError as err:
    print(err)
except:
    print("Unknown Exception Error")
