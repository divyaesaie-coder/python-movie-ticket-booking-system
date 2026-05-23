#Movie ticket booking
#Check seat availability, book seats, update remaining seats.
available_seats=10
booked_seats=0
while True:
    print("1)BOOK TICKETS:")
    print("2)CHECK SEATS AVAILABILITY:")
    print("3)CANCEL BOOKINGS:")
    print("4)EXIT:")
    ch=input("CHOOSE:")
    if ch=="1":
        seats=int(input("ENTER HOW MANY TICKETS:"))
        if seats<=available_seats:
            available_seats=available_seats-seats
            booked_seats=booked_seats+seats
            print("BOOKED!!")
        else:
            print("HOUSE FULL!!")
    if ch=="2":
        print(available_seats)
    if ch=="3":
        tickets=int(input("ENTER HOW MANY TICKETS:"))
        if tickets+available_seats>10:
            print("WRONG TICKETS")
        else:
            available_seats=tickets+available_seats
            booked_seats=booked_seats-tickets
        print("AVAILABLE SEATS:",available_seats)
        print("BOOKED SEATS:",booked_seats)
    if ch=="4":
        print("THANK YOU FOR VISITING!!BYE!!")
        break
