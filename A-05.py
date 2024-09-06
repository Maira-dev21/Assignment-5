# Using conditional statements, check if the number is:
#  - Even or Odd.
#  - Positive, Negative, or Zero.
#  - Whether it is divisible by both 2 and 3 or anyone of them or 
#  not divisible by both check all the cases and print statement for each case.
number = int(input("Enter a number: ")) 
    # Check if number is even or odd   
if(number %2 == 0):
    print(number , "is an even number")
else:
    print(number , " is an odd number")      

 # Check if number is positive, negative, or zero
if (number > 0):
  print(f"{number} is a Positive Number")
elif  (number < 0):  
  print(f"{number} is a Negative Number")
else:
  print(f"{number} is Zero")
# Whether it is divisible by both 2 and 3 or anyone of them
if (number %2 ==0 and number %3 ==0) :
  print(f"{number} is divisible by both 2 and 3")
elif (number %2 ==0) :
  print(f"{number} is divisible by 2")
elif (number %3 ==0) :
  print(f"{number} is divisible by 3")
else :
  print(f"{number} is not divisible by 2 or 3")
#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."
# Take the user's age
age = int(input("Enter your age: "))

# Check if age is 18 or above
if age >= 18:
    # Ask for nationality
    nationality = input("Do you have a nationality of 'Pakistani'? (yes/no): ")
    # Check nationality
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You must be 18 or older to vote.")
#  - Write a program that takes the age of a person as input
#  and determines whether they are a child (0-12 years),
#  teenager (13-19 years), adult (20-59 years), or senior 
# citizen (60 years and above)
ageperson = int(input("Enter age person:"))
if ageperson >= 0 and ageperson <= 12:
 print("you are child")
elif  ageperson >= 13 and ageperson <= 19:
  print("You are Teenager")
elif  ageperson >= 20 and ageperson <= 59:
  print("You are Adult")
else :
  print("You are Senior Citizen")
#  - Enter a month (as a number between 1 and 12). Print 
# the number of days in that month. Assume a non-leap year.
#  - Check if a year is a leap year or not.
year = int(input("Enter a year: "))
if year %4 ==0  :
 print ("This is a leap year")
else :
   print("This is not a leap year")
  # complete