#Q3 set alarm clock
current_time = int(input("What is the current time (in hours)? "))
waiting_time = int(input("How many hours do you have to wait? "))

hours = current_time + waiting_time

alarm_time = hours % 24

print(alarm_time)


#Q4 return day
starting_day = int(input("What is the starting day? "))
stay_length = int(input("What is the length of your stay? "))

days = starting_day + stay_length

return_date = days % 7

print(return_date)


#Q5 separate variable
word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "makes"
word7 = "Jack"
word8 = "a"
word9 = "dull"
word10 = "boy."

print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)


#Q7 compound interest
P = 10000
n = 12
r = 0.08

t = int(input("Compound for how many years? "))

final = P * ( ((1 + (r/n)) ** (n * t)) )

print ("The final amount after", t, "years is", final)


#Q8 circle area
radius = int(input("Input the radius: "))

print (3.14*radius**2)


#Q9 rectangle area
width = int(input("Width: "))
height = int(input("Height: "))

print("The area of rectangle :", width * height)


#Q10 MPG
M = int(input("Enter the number of miles driven: "))
G = int(input("Enter the number of gallons used: "))

print("MPG for a car:", M/G)


#Q11 convert degrees celsius to degrees fahrenheit
deg_c = int(input("What is the temperature in Celsius? "))

deg_f = deg_c * (9 / 5) + 32

print(deg_c, " degrees Celsius is", deg_f, " degrees Farenheit.")


#Q12 convert degrees fahrenheit to degrees celsius
deg_f = int(input("What is the temperature in Fahrenheit? "))

deg_c = (deg_f-32) * 5 / 9

print(deg_f, " degrees Fahrenheit is", deg_c, " degrees Celsius.")


