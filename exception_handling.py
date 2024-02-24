try:
    print("x")
except NameError:
    print("varibale x is not define")
except ZeroDivisionError:
    print("Divided by zero error")
else:
    print("no error")
finally:
    print("Try catch finished")


# # raise an exception if condition true
# x = -1
# if x < 0:
#     raise Exception("Number should be greater than zero")