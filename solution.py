import os
import math


def q1(s):
    # this is a set literal
    vowels = {"a", "e", "i", "o", "u"}  # sorry y
    num_vowels = 0
    num_consonants = 0
    for char in s:
        if char in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

    if num_vowels == num_consonants:
        return None
    # This is valid Python! It will evaluate the expression and return True or False
    return num_vowels > num_consonants


def q2(r, h):
    return math.pi * h * r ** 2


def q3(string_list):
    return ",".join(string_list)


def q4(list_of_lists):
    filename = "output.csv"
    with open(filename, "w") as f:
        for l in list_of_lists:
            f.write(q3(l))  # we can reuse our work from earlier
            f.write("\n")
    return filename


def q5(csvfile):
    result = []
    with open(csvfile) as f:
        for row in f:
            result.append(row.split(","))
    return result


def q6(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Couldn't divide by zero")


def q7(int_list):
    # just convert to a set to eliminate duplicates, then convert back
    return list(set(int_list))


def q8():
    os.mkdir("hw3-folder")
