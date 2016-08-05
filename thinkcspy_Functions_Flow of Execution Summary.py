def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)

# 1, 5, 9, 10, 6, 2, 3, 7, 11
# Python starts at line 1, notices that it is a function definition and skips over all of the lines in the function definition until it finds a line that it no longer included in the function (line 5). It then notices line 5 is also a function definition and again skips over the function body to line 9. On line 10 it notices it has a function to execute, so it goes back and executes the body of that function. Notice that that function includes another function call. Finally, it will return to line 11 after the function square is complete.
