class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        
        seat_list = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append("0")
            seat_list.append(row)
        self._seats[show_id] = seat_list 

    def bookseats(self,show_id,num_tickets,row,col):
        print("-------------------Seat Booking Result!------------------")
        if show_id in self._seats:
            for i in range(num_tickets):
                if self._seats[show_id][row][col] == "0":
                    self._seats[show_id][row][col] = "1" 
                    print(f"Succesfully ! Ticket booked for Show ID {show_id} at seat ({row}, {col})")
                    col += 1
                else:
                    print(f"Seat ({row}, {col}) is already booked.Please choose another seat.")
                    col += 1
        else:
            print("Invalid show ID !")
        print("--------------------------End----------------------------")    


    def viewshow_list(self):
        print("----------------ALL SHOW TODAY--------------")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        print("----------------------END-------------------")
        
    def view_availableseats(self, show_id):
        print("-------------------AVAILABLE SEATS-------------------")
        if show_id in self._seats:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self._seats[show_id][i][j] == "0":
                        print(f"Available Seat: ({i}, {j})")
        else:
            print("Invalid show ID !")
        print("-------------------------END-------------------------")

    def print_seats_matrix(self, show_id):
        print("------SEAT MATRIX-------")
        if show_id in self._seats:
            for row in self._seats[show_id]:
                print(" ".join(row))
        else:
            print("Invalid show ID!")
        print("--------END------------")

hall1 = Hall(10, 10, 1)
hall1.entry_show('s1','Movie1','07:00 PM')
hall1.entry_show('s2','Movie2','09:00 PM')
hall1.entry_show('s3','Movie3','11:00 PM')
print("\n")
print("--WELCOME BACK!--")
print("--Cinema Hall Systems--")

while True:
    print("-----------------------")
    print("1: VIEW ALL SHOW TODAY")
    print("2: VIEW AVAILABLE SEATS")
    print("3: BOOK TICKET")
    print("4: EXIT")
    print("-----------------------")

    option = int(input("1. ENTER OPTION:"))
    
    if option == 1:
       hall1.viewshow_list()
    elif option == 2:
        show_id = input("   1: ENTER SHOW ID:")
        hall1.view_availableseats(show_id)
        hall1.print_seats_matrix(show_id)
    elif option == 3:
        show_id = input("    1: ENTER SHOW ID:")
        numbers_of_ticket = int(input("    2: NUMBERS OF TICKET:"))
        seat_row = int(input("    3: ENTER ROW NO:"))
        seat_col = int(input("    4: ENTER COL NO:"))
        hall1.bookseats(show_id,numbers_of_ticket,seat_row,seat_col)
    elif option == 4:
        print("EXIT SUCCESFULLY!")
        break
