# Calculate the multiplication and sum of two numbers. Given two integerd numbers return their product only if the product is equal or lower than 1000, else return their sum
# I did not use the return function i used print function instead
x = 300
y = 200
sum_xy = x + y
product_xy = x * y
if product_xy <= 1000:
    print(product_xy)
else:
    print(sum_xy)    

 # 2.  Print the sum of the current number and the previous numnmber
 # Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number
previous_num = 0
for num in range(1,11):
    sum_x = previous_num + num
    print(f"current number: {num}, previous number: {previous_num}, sum of current and previous number: {sum_x}")
    previous_num = num