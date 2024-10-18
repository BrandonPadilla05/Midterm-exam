# I could not figure out how to do question number 1

# Question number 2 on midterm
def transform_data():
    # Step 1: Prompt the user for input (list of integers separated by spaces)
    user_input = input("Enter a list of integers separated by spaces: ")
    
    # Step 2: Convert the input string into a list of integers
    int_list = list(map(int, user_input.split()))
    
    # Step 3: Create a new list with each integer squared
    squared_list = [x ** 2 for x in int_list]
    
    # Step 4: Calculate the sum of the squared values
    squared_sum = sum(squared_list)
    
    # Step 5: Return both the new list and the sum
    return squared_list, squared_sum

# Calling the function
squared_values, total_sum = transform_data()
print("Squared List:", squared_values)
print("Sum of Squares:", total_sum)
