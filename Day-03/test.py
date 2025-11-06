y = 20  # Global variable

def another_function():
    y=10
    print(f"value is {y}")  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20