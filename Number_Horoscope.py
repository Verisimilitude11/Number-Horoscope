first_name = int(input("How many letters are in your first name? "))
last_name = int(input("How many letters are in your last name?"))
first_name = int(input("How many letters are in your first name? "))
last_name = int(input("How many letters are in your last name? "))

month = int(input("What month were you born in? (January = 1) "))
day = int(input("What day were you born in? "))

print("")
print("Your fortune:")

sum1 = first_name + last_name
sum2 = month + day
love = sum1 * sum2

print("It will be " + str(love) + " days until you fall in love.")

total = 0
total += first_name
total += last_name
total += month
total += day
total2 = month + day
event = total % total2

print("In " + str(event) + " days, an important event will happen in your life.")

unlucky = month - first_name
total = 0
total += first_name
total += last_name
total += month
total += day
total2 = month + day
event = total % total2

print("In " + str(event) + " days, an important event will happen in your life.")

unlucky = month - first_name
print("Stay away from the number " + str(unlucky))
