number = int(input("Please enter a number: "))
sum_of_odd_nums = 0
sum_of_even_nums = 0
even_num_counter = 0
for i in range(1, number+1):
    if i % 2 != 0:
        sum_of_odd_nums += i
    else:
        sum_of_even_nums += i
        even_num_counter += 1
print("sum of odd numbers: ", sum_of_odd_nums)
print("average of even numbers: ", sum_of_even_nums / even_num_counter)
