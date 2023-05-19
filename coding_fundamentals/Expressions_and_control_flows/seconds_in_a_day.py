current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

total_number_of_seconds_in_a_day = 24 * 60 * 60
remaining_seconds = total_number_of_seconds_in_a_day - (current_hours * 60 * 60 + current_minutes * 60\
                                                        + current_seconds)
print("Remaining seconds: ", remaining_seconds)