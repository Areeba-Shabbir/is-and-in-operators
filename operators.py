               ##   IS OPERATORS   ##
             # EXAMPLE 1 : COMPARING LIST #
a = [1,2,3]
b = a
c = [1,2,3]

print (a is b)  # True (both print to the same object)
print (a is c) # false (different objects with the same value)


             # EXAMPLE 2 : COMPARING INTEGERS #
x = 100
y = 100
print ( x is y ) # True (small integers are cached in python)

             # EXAMPLE 3 #

x = None
y = None
print ( x is y )   # True

             # EXAMPLE 4 : COMPAING STRINGS #
str1 = "hello"
str2 = "hello"
print (str1 is str2) #True

            # EXAMPLE 5 : CHCKING IDENTITY WITH BOOLEAN VALUES #
a = True
b = True
print ( a is b ) # True

              ## IN OPERATORS ##
            # EXAMPLE 1 #
FRUITS = [ "apple", "banana", "strawberry"]
print ("banana" in FRUITS) # True
print ("Cherry" in FRUITS) # False


          # EXAMPLE 2 #  
text = "Hello"
print ("H" in text) # True 
print ("hello" in text) # False (case sensitive)

 
         # EXAMPLE 3 #
student = { "name" : "Areeba", "age" : 22, "course" : "python"}
print ( "name" in student) # True
print ( "Areeba" in student) # False (only check keys not values)

          # EXAMPLE 4 #
numbers = (10, 20, 30, 40)
print (30 in numbers) #True
print ( 50 in numbers) # False


             # EXAMPLE 5 #
colors = { "red", "blue", "black"}
print ("blue" in colors) # True
print ( "purple" in colors) # False






