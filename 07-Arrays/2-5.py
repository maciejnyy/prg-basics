# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total_seats = 0
   for row in seats:
      for seat in row:
         total_seats += 1
         
   return total_seats

def seats_available(seats):
   available_seats = 0
   for row in seats:
      for seat in row:
        if seat == 'A':
           available_seats += 1
        else:
           continue

   return available_seats

def seats_booked(seats):
   booked_seats = 0
   for row in seats:
      for seat in row:
        if seat == 'B':
           booked_seats += 1
        else:
           continue

   return booked_seats

def seat_status(seats, row, place):
   for i in range(len(seats)):
      for j in range(len(seats[i])):
        if i == row-1 and place-1 == j:
           return seats[i][j]

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,3))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))