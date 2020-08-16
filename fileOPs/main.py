# This Python file uses the following encoding: utf-8

pd.read_csv()

def lesser_of_two_elements(a,b):
    if (a%2 == 0 and b%2==0):
        if (a < b):
            print(a)
        else:
            print(b)
    else:
        if (a > b):
            print(a)
        else:
            print(b)

lesser_of_two_elements(2,4)

def animal_cracker(*args):
   return args[0][0].lower() == args[1][0].lower()


print(animal_cracker("deniz","danturk"))

def makes_twenty(a,b):
    if a+b == 20 :
        return True
    else:
        return False

def makes_twenty1(a,b):
    return (a+b)== 20 or a == 20 or b ==20

print(makes_twenty(15,3))
print(makes_twenty1(20,5))

def old_Mac(str):
    str1=""
    for item in range(len(str)):
        print(item)
        if item == 0 or item == 3:
            str1 = str1 + str[item].upper()
        else:
            str1 = str1 + str[item].lower()
    return str1


print(old_Mac("DenizCanrturk"))

def reverse(str):
    words = str.split()
    words = list(reversed(words))
    print(" ".join(words))

reverse("deniz can tufk sldf soak")

def within(args):
    if (args >= 90 and args <= 110) or (args >= 190 and args <= 210):
        return True
    else:
        return False

print(within(195))

def find4(nums):
    for x in nums:
        if (nums[x] == 2) and (nums[x+1] == 2):
            return True


def find5(nums):
    for x in range(len(nums)-1):
        if (nums[x] == 3) and (nums[x+1] == 3):
            return True
    return False

def has22(lst):
     lst = iter(lst)
     for i in lst:
             try:
                 if i == 2 and lst.next() == 2:
                     return True
             except StopIteration:
                     pass
     return False

has22([6,3,5,9,8,5,4,5,6,98,7])

def triple(str):
    str1=""
    for idx in range(len(str)):
        str1 = str1 + str[idx]*3
    print(str1)
triple("Mississippi")

def oo7(nums):
    for x in range(len(nums)-2):
        if (nums[x] == 0) and (nums[x+1] == 0 and (nums[x+2]== 7 )):
            print("true")
            return True
    print("false")
    return False

oo7([0,0,47,8,6,5,4,4])

def myfunc(r):
    return r*r
