
# creating function# 1 to calculate the (TOTAL HOTEL-COST)

def hotel_cost(num_nights, stay_per_night=55): # We get the num_nights from user/customer &  the price for stay_per_night is assigned 

    total_cost = num_nights * stay_per_night   # Multiplying the 'num_nights & stay_per_night'
    print("The total-cost for your hotel-stay is: ", f"{num_nights} * {stay_per_night} = {total_cost}") # Calculation is displayed
    print()
    return total_cost                    # the total-cost for the hotel-stay is displayed when we call this this function each-time


# creating function# 2 to calculate the (PLANE-COST)

def plane_cost(city_flight): # Providing the flight-option to choose it from the lists to the user

    # using the condition to validate the option chosen by the user
    if(city_flight == "Edinburgh" or city_flight == "edinburgh" or city_flight == "EDINBURGH"): 

        flight_cost = 71            # if above condition is true then this amount is assigned to it
        print("The plane-cost for the city that you have chosen is: ", flight_cost) # displaying the flight-cost
        print()
        return flight_cost
    
    elif(city_flight == "Dublin" or city_flight=="dublin" or city_flight=="DUBLIN"):

        flight_cost = 150
        print("The plane-cost for the city that you have chosen is: ", flight_cost)
        print()
        return flight_cost
    
    elif(city_flight=="London" or city_flight=="london" or city_flight=="LONDON"):
        
        flight_cost = 429
        print("The plane-cost for the city that you have chosen is: ", flight_cost)
        print()
        return flight_cost
    
    else:              # if the user chosen an option that is not available then it will display the below 'print-message'              
        print("Your option is not available at this time, so please choose it from the available-list")
        print()
        return 0


# creating function# 3 to calculate the (TOTAL CAR-RENTAL_COST)

def car_rental(rental_days, rental_per_day=16):  # We get the rental_days from user &  the price for rental_per_day is assigned 

    total_cost = rental_days * rental_per_day    # Multiplying the 'rental_days & rental_per_day'
    print("The total-cost for your car-rental is: ", f"{rental_days} * {rental_per_day} = {total_cost}") # Calculation is displayed
    print()
    return total_cost                     # the total-cost for the car_rental is displayed when we call this this function each-time

# creating function# 4 to calculate the (TOTAL HOLIDAY-COST)
def holiday_cost(hotel_cost, plane_cost, car_rental): # Here, we combine the above 3 functions in order to do the total-calculation

    total_cost = hotel_cost + plane_cost + car_rental # Adding the total-values of the above 3 functions
    print("----------------------------------------------------------") # creating a line to display the total-value
    print("The total-cost for your holiday is : ", f"{hotel_cost} + {plane_cost} + {car_rental} = {total_cost}") #Displaying in total 
    print()
    return total_cost            # the total-cost for the holiday is displayed when we call this this function each-time


# Creating an option for the user to enter 'city_flight' where they want to travel
city_flight = str(input("Please enter the city name where you want to fly from the list- 1)Edinburgh 2)London 3)Dublin: "))

# using condition to validate the user's input is within the list
if(city_flight == "Edinburgh" or city_flight == "edinburgh" or city_flight == "EDINBURGH" or city_flight == "Dublin" 
   or city_flight=="dublin" or city_flight=="DUBLIN" or city_flight=="London" or city_flight=="london" or city_flight=="LONDON"):
        
        print("Thanks for choosing from the list")
        print()

# If user's optin is not in the list then this condition will print the below 'print-message'
else:
    print("Your option is not available at this time, so please choose it from the available-list")
    print()
    exit()

# getting the inputs from the user
num_nights = int(input("Please enter the number of nights for staying at a hotel: "))
print()
rental_days = int(input("Please enter the number of days that you will be hiring a car: "))
print()

# Calling all the created 4 functions to execute the calculations
hotel_result = hotel_cost(num_nights)
plane_result = plane_cost(city_flight)
car_result = car_rental(rental_days)
holiday_result = holiday_cost(hotel_result, plane_result, car_result)