"""
Fibinnocci Series is the sequence in which each number is the sum of the two preceding ones


"""

# def fibinocci_series(numb):
#     if numb < 0:
#         return "Enter a valid fibinocci number"
#     else:
#         n1,n2= 0,1
#         sum=0
#         for i in range(0, numb):
#             n1 = n2
#             n2= sum
#             sum = n1+ n2
#             print(sum)


def fibinocci_recursion(numb):
    if numb <= 1:
        return numb
    return fibinocci_recursion(numb-1) + fibinocci_recursion(numb - 2)


if __name__=="__main__":
    # fibinocci_series(5).
    number = 10

    for i in range(number):
        print(fibinocci_recursion(i))