#### ---- INPUT ---- ####

# Get INPUT asking how many letters are in their first
# name, then ASSIGN to first_name
# (Hint: TYPECAST)
first_name = int(input("How many letters are in your first name? "))

# Get INPUT asking how many letters are in their last
# name, then ASSIGN to last_name
# (Hint: TYPECAST)
last_name = int(input("How many letters are in your last name?"))

#### ---- INPUT ---- ####

# Get INPUT asking how many letters are in their first
# name, then ASSIGN to first_name
# (Hint: TYPECAST)
first_name = int(input("How many letters are in your first name? "))

# Get INPUT asking how many letters are in their last
# name, then ASSIGN to last_name
# (Hint: TYPECAST)
last_name = int(input("How many letters are in your last name? "))

# Get INPUT asking the month they were born in as a
# number (January = 1, December = 12), then ASSIGN
# to month. (Hint: TYPECAST)
month = int(input("What month were you born in? (January = 1) "))

# Get INPUT asking what day of the month they were born
# on, then ASSIGN to day (Hint: TYPECAST)
day = int(input("What day were you born in? "))

# PRINT a blank line
print("")
# PRINT "YOUR FORTUNE:"
print("Your fortune:")


#### ---- LOVE CALCULATION ---- ####

# ADD first_name and last_name, then ASSIGN to sum1
sum1 = first_name + last_name

# ADD month and day variables, then ASSIGN to sum2
sum2 = month + day

# MULTIPLY sum1 and sum2, then ASSIGN to love
love = sum1 * sum2

# PRINT "It will be " CONCATENATED with love variable,
# CONCATENATED with " days until you fall in love."
# (Hint: TYPECAST)
print("It will be " + str(love) + " days until you fall in love.")


#### ---- EVENT CALCULATION ---- ####

# Create variable called total, ASSIGN it the value 0.
total = 0

# INCREMENT total by first_name
total += first_name

# INCREMENT total by last_name
total += last_name

# INCREMENT total by month
total += month

# INCREMENT total by day
total += day

# ADD together month and day again, ASSIGN to total2
total2 = month + day

# Get MODULUS of total and total2, ASSIGN to event
event = total % total2

# PRINT "In " CONCATENATED with event, CONCATENATED
# with " days, an important event will happen in
# your life." (Hint: TYPECAST)
print("In " + str(event) + " days, an important event will happen in your life.")


#### ---- UNLUCKY NUMBER CALCULATION ---- ####

# SUBTRACT first_name from month, then ASSIGN to
# unlucky.
unlucky = month - first_name

# PRINT "Stay away from the number " CONCATENATED with
# the variable unlucky (Hint: TYPECAST)
print("Stay away from the number " + str(unlucky))


# Turn in your Coding Exercise.
nt(input("How many letters are in your last name? "))

# Get INPUT asking the month they were born in as a
# number (January = 1, December = 12), then ASSIGN
# to month. (Hint: TYPECAST)
month = int(input("What month were you born in? (January = 1) "))

# Get INPUT asking what day of the month they were born
# on, then ASSIGN to day (Hint: TYPECAST)
day = int(input("What day were you born in? "))

# PRINT a blank line
print("")
# PRINT "YOUR FORTUNE:"
print("Your fortune:")


#### ---- LOVE CALCULATION ---- ####

# ADD first_name and last_name, then ASSIGN to sum1
sum1 = first_name + last_name

# ADD month and day variables, then ASSIGN to sum2
sum2 = month + day

# MULTIPLY sum1 and sum2, then ASSIGN to love
love = sum1 * sum2

# PRINT "It will be " CONCATENATED with love variable,
# CONCATENATED with " days until you fall in love."
# (Hint: TYPECAST)
print("It will be " + str(love) + " days until you fall in love.")


#### ---- EVENT CALCULATION ---- ####

# Create variable called total, ASSIGN it the value 0.
total = 0

# INCREMENT total by first_name
total += first_name

# INCREMENT total by last_name
total += last_name

# INCREMENT total by month
total += month

# INCREMENT total by day
total += day

# ADD together month and day again, ASSIGN to total2
total2 = month + day

# Get MODULUS of total and total2, ASSIGN to event
event = total % total2

# PRINT "In " CONCATENATED with event, CONCATENATED
# with " days, an important event will happen in
# your life." (Hint: TYPECAST)
print("In " + str(event) + " days, an important event will happen in your life.")


#### ---- UNLUCKY NUMBER CALCULATION ---- ####

# SUBTRACT first_name from month, then ASSIGN to
# unlucky.
unlucky = month - first_name

# PRINT "Stay away from the number " CONCATENATED with
# the variable unlucky (Hint: TYPECAST)
print("Stay away from the number " + str(unlucky))
