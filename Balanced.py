def balanced(input_string):
    # Only expects x and y
    # Get the count of x and y. If equal then print true, otherwise print false
    x_count = input_string.count("x")
    y_count = input_string.count("y")

    if x_count == y_count:
        print 'True'
    else:
        print 'False'

def balance_bonus(input_string):
    # Get the frequency each letter appears in the string. Put into a dictionary
    frequency_dict = {}

    for i in input_string:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    # If the values in the dict don't equal the max value then print false. Otherwise print true
    print all(value == max(frequency_dict.values()) for value in frequency_dict.values()) # Returns true or false


balanced(input_string="")
balance_bonus(input_string="")


