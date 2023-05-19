# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

daily_coding_hours = 6
workdays = 5
duration_of_the_semester_in_weeks = 17

coding_hours_in_a_semester = daily_coding_hours * workdays * duration_of_the_semester_in_weeks
print("The hours spent with coding in a semester by an attendee are: ", str(coding_hours_in_a_semester) + "hrs")

weekly_work_hours = 52
total_work_hours_in_a_semester = weekly_work_hours * duration_of_the_semester_in_weeks
percentage_of_coding_hours_in_a_semester = \
    (coding_hours_in_a_semester / total_work_hours_in_a_semester) * 100
print("Percentage of coding hours in a semester: ", str(percentage_of_coding_hours_in_a_semester) + "%")
