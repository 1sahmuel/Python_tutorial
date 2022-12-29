#While loop


#i = 1
#while i <=5:
 #   print(i)
  #  i  += 1
#print("done")

#i = 1
#while i <=5:
 #   print("x" * i)
  #  i  += 1
#print("done")

#Exercise
#initial_guess=  9
#number_of_chances= 0
#while number_of_chances < 3:
#    User_guess = int(input("Enter guess number: "))
 #   number_of_chances +=1
  #  if User_guess == initial_guess:
   #     print("You win!!!")
    #    break
#else:
 #    print("you lose!!!")

          #Car GAme
#button = ""
#option_help = "help"
#start_button = "start"
#stop_button = "stop"
#quit_button = "quit"

#while button != "quit":
    
    #button = input("> ")
    #if button == option_help:
     #   print("""start - to start yhe car \nstop - to stop the car \nquit - to exit""" )
    
   # elif button == start_button:
    #    print("Car started... Ready to go!")
    #elif button == stop_button:
     #   print("Car stopped.")
    #elif button != option_help:
     ### break
#else:
 #   print("exit game")

    #For loop
#for item in "samuel":
 #    print(item)

#for num in range(10,1000):
   # print(num)

    #EXERCISE

#prices = [10, 20, 30]
#total = 0
#for item in range(5):
 #   total += item
#print(total)

        #NESTED LOOP

#shape = [ 2,2,2,2,5]
#for f_shape in shape:
 # print("x" * f_shape)

 #alternatively using Nested loop
#number = [5, 2, 5, 2, 2]
#for X in number:
  #output = ''
  #for y in range(X):
   # output += 'x'
  #print(output)


  #List
#name = [ 'john', 'sam', 'mosh', 'boo ']
#print(name[3])
 

#Write a program to find the largest number in a list
#number = [ 3,5,10,4,6]
#max = number[2]
#for large in number:
 # if large > max:
  #  max = large
#print(max)

# 2d List
#matrice

#matrix = [ 
 ###[7, 8, 9]
#]

#print(matrix[0][2])

#for row in matrix:
 # for numbers in row:
  #  print(numbers)

#List 
numbers = [ 2,4,6,4,9,0]
count = []
for num in numbers:
  if num not in count:
    count.append(num)
print(count)


