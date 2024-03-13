"""
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.

"""


class PivotNumber(object):
    def is_pivot_number(self, numb):
        lst_ = [i for i in range(1,numb+1)]
        pivot = round(len(lst_)/2)
        while pivot < len(lst_):
            if sum(lst_[:pivot+1]) == sum(lst_[pivot:]):
                return lst_[pivot]
            pivot+=1
        return -1
    


if __name__ == "__main__":
    print(PivotNumber().is_pivot_number(8))
