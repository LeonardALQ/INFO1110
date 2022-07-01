# Name: Leonard Alqaseer
# unikey: malq6239
import sys 

print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome to Pizzaz cinema ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-=-=-=-=-=-=-=-=-=-=-=-=-=-=""".strip())

data = [ 
"The Shining. 1980. 2h 26m. 10:00. Room 1",
"Your Name. 2016. 1h 52m. 13:00. Room 1",
"Fate/Stay Night: Heaven's Feel - III. Spring Song. 2020. 2h 0m. 15:00. Room 1",
"The Night Is Short, Walk on Girl. 2017. 1h 32m. 17:30. Room 1",
"The Truman Show. 1998. 1h 47m. 19:30. Room 1",
"Genocidal Organ. 2017. 1hr 55m. 21:45. Room 1",

"Jacob's Ladder. 1990. 1h 56m. 10:00. Room 2",
"Parasite. 2019. 2h 12m. 12:15. Room 2",
"The Dark Knight. 2008. 2h 32min. 14:45. Room 2",
"Blade Runner 2049. 2017. 2h 44m. 17:45. Room 2",
"The Mist. 2007. 2h 6m. 21:00. Room 2",
"Demon Slayer: Mugen Train. 2020. 1h59min. 23:20. Room 2",

"The Matrix. 1999. 2h 16m. 10:00. Room 3",
"Inception. 2010. 2h 42m. 11:30. Room 3",
"Shutter Island. 2010. 2h 19m. 14:30. Room 3",
"Soul. 2020. 1hr 40m. 17:00. Room 3",
"Mrs. Brown. 1997. 1h 41min. 19:00. Room 3",
"Peppa Pig: Festival of Fun. 2019. 1h 8min. 21:00. Room 3",
"Titanic. 1997. 3h 30min. 22:15. Room 3" ]

#Functions:
def end_of_program(): 
    print("\nBye.")
    exit()

#Compares the requested time with the data array and returns the lines which match with that time 
def get_movie(requested_time):  
    int_time = int(time[i][1:3] + time[i][4:6])
    if time[i] in case_insensitive_data[i] and int_time >= requested_time:
        return data[i]

#Iterates through each Australian Currency and checks if it should return that currency as change 
#If it does, then it saves how many times it should return that currency in a counter 
def calculate_change(change): 
    while change != 0: 
        change = round(float(change), 2)
        for i in range(len(au_currency)):
            if au_currency[i] <= change: 
                change = change - au_currency[i] 
                counter[i] += 1 
                break
    return counter

#Checks if the payment is divisible by 5c i.e. is a valid payment 
def is_valid_payment(amount_paid): 
    amount_paid = float(amount_paid)
    if (amount_paid*1e10 % 5e8)/1e10 != 0: 
        return False 
    else: 
        return True 

#Mirrors the functionality of sum() since it wasn't recommended to use it... 
def lst_sum(lst): 
    lst_sum = 0
    for i in range(len(lst)):
        lst_sum += lst[i]
    return lst_sum

#Checks if the requested movie is in the data,
def movie_found(requested_movie): 
    if requested_movie not in movie_data: 
        return False 
    else: 
        return True 

#Check if a switch command is given or not
if len(sys.argv) == 1:
    print("Usage: python3 pizzaz.py [--show <timenow> | --book | --group]")
    exit() 
else: 
    switch = sys.argv[1]

#Check if appropriate switch commands are given and if any unacceptable extras are given: 
if (len(sys.argv) > 3 or not(switch == "--show" 
        or switch == "--book" 
        or switch =="--group")): 
    print("\nSorry. This program does not recognise the switch options.\n\nBye.")
    exit()

#Global Variables Initialization:  
(movie_data, time, case_insensitive_data) = [], [], []

#How I access the data: 
#Makes all the data case-insensitive 
for i in range(len(data)): 
    case_insensitive_data.append(data[i].lower())

#Iterates through the data and stores each single bit of data into a list 
for i in range(len(data)):
    seperated_data = case_insensitive_data[i].split(".") 
    for i in range(len(seperated_data)):
        #Checks for special cases like "Mrs. Brown" or "Spring Song": 
        if seperated_data[i][0].isalpha() and seperated_data[i+1][1].isalpha():
            movie_data.append((seperated_data[i] + "." + seperated_data[i+1]))
        elif seperated_data[i] in {" spring song", " brown"}:
            continue
        else: 
            movie_data.append(seperated_data[i])

#Singles out the time of the movies and puts it all in a list  
for i in range(len(movie_data)): 
    if ":" in movie_data[i] and movie_data[i][1].isdigit(): 
        time.append(movie_data[i])


if switch == "--show": 
    #Checks for a timenow switch 
    if len(sys.argv) != 3:
        print("\nSorry. This program does not recognise the switch options.")
        end_of_program()

    #Checks the format of that timenow switch 
    elif (len(sys.argv[2]) != 5
    or (not (sys.argv[2][0:2].isdigit() 
    and sys.argv[2][3:5].isdigit()
    and sys.argv[2][2] == ":"))): 
        print("\nSorry. This program does not recognise the time format entered.")
        end_of_program()
    #If the format is correct, read the input as integer and by ignoring the ":" in between
    else: 
        hours = sys.argv[2][0:2]
        minutes = sys.argv[2][3:5]
        requested_time = int(hours + minutes)

    #Checks if the input is larger than 24:00 less than 00:00, or has more than 59 minutes
    #if so, prompt the user with a message
    if int(hours) == 0: 
        if int(minutes) <= 59: 
            pass
        else: 
            print("\nSorry. This program does not recognise the time format entered.")
            end_of_program()

    elif (requested_time != 0
    and (requested_time >= 2400 
    or requested_time < 0
    or int(minutes) > 59)): 
        print("\nSorry. This program does not recognise the time format entered.")
        end_of_program()

    #Calls the function to get movie, and iterates through the results that match 
    for i in range(len(data)):
        requested_movie = get_movie(requested_time)
        if requested_movie != None: 
            print(requested_movie)
    
    end_of_program()
 
elif switch == "--book" or switch == "--group": 
    #Variables
    (popcorn_size_list, popcorn_cost, number_of_popcorns) = [], [], 0

    #Checks if any extra switch arguments are given, if yes, prompt the user with an error 
    if len(sys.argv) > 2:
        print("\nSorry. This program does not recognise the switch options.")
        end_of_program()

    requested_movie = input("\nWhat is the name of the movie you want to watch? ").lower()

    #Searches for movie, if not found it asks them to try again or exit. 
    while not movie_found(requested_movie): 
        movie_not_found_try_again = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ").lower()
        if movie_not_found_try_again == "y":
            requested_movie = input("What is the name of the movie you want to watch? ").lower()
        elif movie_not_found_try_again == "n": 
            end_of_program()

    #Sets the parameters so that the common code works for both switches  
    if switch == "--book":
        number_of_customers = 1

    #Sets the parameters so that the common code works for both switches 
    #and executes other required functionalities for the group switch 
    elif switch == "--group":
        number_of_customers = int(input("\nHow many persons will you like to book for? "))
        print("")
        #Checks if there is at least 2 people in the group, if not prompt the user with a message
        if number_of_customers <= 1: 
            small_group_try_again = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit.").lower()
            while not (small_group_try_again == "y" or small_group_try_again == "n"): 
                small_group_try_again = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit.").lower()
            if small_group_try_again == "y":
                number_of_customers = input("How many persons will you like to book for? ")
            elif small_group_try_again =="n": 
                end_of_program() 
        
        #Iterates through the room numbers and saves them to a list to compare later. 
        room_number = []
        for i in range(len(data)): 
            if data[i][-1].isdigit(): 
                room_number.append(data[i][-1])
        
        #Compares the room numbers with the one that the requested movie is in
        #then returns the rooms that match 
        for i in range(len(data)): 
            if requested_movie in case_insensitive_data[i]: 
                requested_room = room_number[i]

        #Saves the capacity of the room in a variable
        if requested_room == "1": 
            requested_room_seats = 36/2 
        elif requested_room == "2": 
            requested_room_seats = 136/2
        elif requested_room == "3": 
            requested_room_seats = 42/2

        #Checks if there is enough room in the room 
        while (number_of_customers > requested_room_seats):
            big_group_try_again = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit. ".
            format(number_of_customers, int(requested_room_seats))).lower()

            while not (big_group_try_again  == "y" or big_group_try_again == "n"): 
                big_group_try_again = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit. ".
                format(number_of_customers, requested_room)).lower()

            if big_group_try_again == "y": 
                number_of_customers = int(input("How many persons will you like to book for? "))
            elif big_group_try_again =="n":
                end_of_program() 
            
        print("")
    
    #Asks each user if they want to order popcorn, and saves calculates the prices 
    for i in range(number_of_customers):
        order_popcorn = ""
        while not (order_popcorn == "y" or order_popcorn == "n"): 
            if number_of_customers > 1: 
                order_popcorn = input("For person {}, would you like to order popcorn? Y/N ".
                format(i+1)).lower()
            else:
                order_popcorn = input("\nWould you like to order popcorn? Y/N ").lower() 
        if order_popcorn == "y":
            number_of_popcorns += 1
            popcorn_size = ""
            while not (popcorn_size == "s" 
            or popcorn_size == "m" 
            or popcorn_size == "l"):
                if number_of_customers > 1: 
                    popcorn_size = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) "
                    .format(i+1)).lower()
                else: 
                    popcorn_size = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ").lower()

            if popcorn_size == "s": 
                popcorn_size_list += ["Small popcorn"]
                popcorn_cost.append(3.5)

            elif popcorn_size == "m": 
                popcorn_size_list += ["Medium popcorn"]
                popcorn_cost.append(5)

            elif popcorn_size == "l": 
                popcorn_size_list += ["Large popcorn"]
                popcorn_cost.append(7) 

        #This is neccessary so that both the customers list and the popcorn list are comparable
        elif order_popcorn == "n": 
            popcorn_cost.append(0)
            popcorn_size_list += ["N/A"]
    
        #saves the requested time of the movie in variable
        for i in range(len(data)):
            if requested_movie in case_insensitive_data[i]:  
                requested_movie_time = int(time[i][1:3] + time[i][4:6])

    print("")
    #Prompts the user with each customer's seat number 
    for i in range(number_of_customers):
        print("The seat number for person {} is #{}".
        format(i+1, 17 if number_of_customers == 1 else (2*(i+1)-1)))

    #Checks when the time of the movie is, and sets the price depending on that 
    if requested_movie_time < 1600: 
        ticket_cost = 13 
        before_or_from_16 = "Ticket before 16:00"
    else: 
        ticket_cost = 15 
        before_or_from_16 = "Ticket from 16:00"

    #Calculates total cost and formats it to 2 d.p
    total_cost = ticket_cost*number_of_customers + lst_sum(popcorn_cost)
    total_cost = "{:.2f}".format(total_cost)
    ticket_cost = "{:.2f}".format(ticket_cost) 

    #Prints initial cost before any discounts 
    print("\nFor {} person{}, the initial cost is ".
    format(number_of_customers,
    "s" if number_of_customers > 1 else "").ljust(34) + "$" + total_cost)
    
    #Breaks the prices into individual parts 
    for i in range(number_of_customers): 

        print(" Person {}: {}".
        format(i+1, before_or_from_16).ljust(34) + "$" + ticket_cost)

        if popcorn_size_list[i] != "N/A": 
            print(" Person {}: {}".
            format(i+1, popcorn_size_list[i]).ljust(34) + "$" + " {:.2f}".
            format(popcorn_cost[i]))

    #Calculates any discount prices and prompts the user with those discounts 
    if float(total_cost) > 100: 
        ticket_discount = round((float(ticket_cost)*0.1*number_of_customers)/0.05) * 0.05
        popcorn_discount = round((lst_sum(popcorn_cost)*0.2)/0.05) * 0.05
        discounted_total_cost = float(total_cost) - popcorn_discount - ticket_discount

        print("\nDiscount applied tickets x{}".
        format(number_of_customers).ljust(33) + " -${}{:.2f}".
        format("" if ticket_discount >= 10.00 else " ", ticket_discount))

        print("Discount applied popcorn x{}".
        format(number_of_popcorns).ljust(33) + "-${}{:.2f}".
        format("" if popcorn_discount >= 10.00 else " ", popcorn_discount))

        print("\nThe final price is".ljust(35) + "${:.2f}".
        format(discounted_total_cost))
    else: 
        print("\n No discounts applied".ljust(35) + "$" + " 0.00")
        print("\nThe final price is".ljust(35) + "$" + total_cost)

    #Calls the is_valid_function to check if payment is divisible by 5c
    #Checks if payment is enough
    amount_paid = float(input("Enter the amount paid: $"))
    while float(amount_paid) < float(total_cost) or not is_valid_payment(amount_paid): 
        if not is_valid_payment(amount_paid):
            print("The input given is not divisible by 5c. Enter a valid payment.")
            amount_paid = float(input("Enter the amount paid: $"))
        elif float(amount_paid) < float(total_cost): 
            print("The user is ${:.2f} short. Ask the user to pay the correct amount.".
            format(float(total_cost) - float(amount_paid)))
            amount_paid = input("Enter the amount paid: $")
    
    #Calculates discount if it applies and prompts the user with their change: 
    if float(total_cost) > 100: 
        change = float(amount_paid) - float(discounted_total_cost)
    else: 
        change = float(amount_paid) - float(total_cost)
    print("Change: ${:.2f}".format(change))

    #Calculates change by iterating through each Australian currency and saving 
    #the amount of times that Australian currency was deducted from the change
    #Then prompts the user with the final amount of change 
    au_currency = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
    counter = [0,0,0,0,0,0,0,0,0,0,0]
    counter = calculate_change(change)
    for i in range(len(au_currency)): 
        if counter[i] !=0: 
            if au_currency[i] < 1:
                print(" {}{:.0f}c: {}".
                format(" " if au_currency[i]*100 < 10 else "",au_currency[i]*100, counter[i]))
            else: 
                print(" ${}{}: {}".
                format(" " if au_currency[i] <10 else "", au_currency[i], counter[i]))

    end_of_program() 
