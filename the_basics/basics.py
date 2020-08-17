def mean(mylist):
    print("Function started!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
my_mean = mean(student_grades)
print(my_mean + 10)