# User prompted to enter a number, test if even or odd
user_input = input("Please enter a number: ")

try:
   val = int(user_input)
   user_number = int(user_input)

   if user_number %2 == 0:
   	print("Your number is even")

   else:
   	print("Your number is odd")

except ValueError:
   print("Please enter a valid number")

