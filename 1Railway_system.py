
train_name = "Rajdhani Express"
train_number = 12951
source_station = "Mumbai"
destination_station = "Delhi"
ticket_price = 2450.75 

print("Welcome to Indian Railway Reservation System")
print("Train Name :", train_name)
print("Train Number :", train_number)
print("Source Station :", source_station)
print("Destination Station :", destination_station) 

print (type(train_name))
print (type(train_number))
print (type(ticket_price))

passenger_name = "Rahul Sharma"
seat_number = "B2-45"
is_confirmed = True

ticket_price_integer = int(ticket_price)
print(type(ticket_price_integer))

train_number_string = str(train_number)
print(type(train_number_string))

passenger_name = "Rahul Sharma"
seat_number = "B2-45"
confirmation_status = "Conformed"

'''
Passenger_name = "Rahul Sharma"
passenger_age = 28
gender = "Male"
mobile_number = 98765432210

train_name = "Rajdhani Express"
seat_number = "B2 - 45"
ticket_price = 2450
journey_date = "25-may-2026"

print("train name:" , train_name)
print("seat number:" , seat_number)
print("ticket price:", ticket_price)
print("journey datae:", journey_date) 

number_of_passengers = 3
ticket_price = 2450

total_fare = number_of_passengers * ticket_price
print("total fare:", total_fare)

gst_percentage = 5

gst_amount = (total_fare * gst_percentage) / 100
print("GST amount:", gst_amount)

final_amount = total_fare + gst_amount
print("final payable amount:" , final_amount)

print("_ _ _ _ indian Railwaly Ticket _ _ _ _ ")
print("passenger name : " , passenger_name)
print("train name : " , train_name)
print("seat number : " , seat_number)
print("journey date : " , journey_date)
print("passengers : " , number_of_passengers)
print("ticket fare : " , total_fare)
print("GST amount : " , gst_amount)
print("Final amount : " , final_amount)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
Lab 3
'''
passenger_name = "Rahul Sharma"
ticket_status = "Confirmed"

if ticket_status == "Confirmed":
 	print("Ticket is Confirmed")

waiting_list = 3   

if waiting_list == 0:
 	print("Ticket Confirmed")
else:
 	print("Ticket is in Waiting List")

ticket_status = "RAC"    

if ticket_status == "Confirmed":
 	print("Seat Allocated Successfully")
elif ticket_status == "RAC":
 	print("Partial Reservation Available")
else:
 	print("Ticket is in Waiting List")

age = 65
if age >= 60:
 	print("Passenger Eligible for Senior Citizen Discount") 

age = 65
is_ticket_confirmed = True

if age >= 60 and is_ticket_confirmed == True:
 	print("Passenger eligible for Senior Citizen Benefits")

ticket_status = "Confirmed"
payment_status = "Paid"

if ticket_status == "Confirmed" and payment_status == "Paid":
 	print("Ticket Successfully Booked")
elif ticket_status == "RAC":
 	print("Partial Seat Reservation Available")
else:
 	print("Booking Pending")

