def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # Call the inner function

outer_function()  # Call the outer function
