seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None,  "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

seat_available = [ ]
for row_index, row in enumerate(seats):  
    row_index += 1 
    for seat_index, seat in enumerate(row): 
        seat_index += 1
        if seat == None: 
            print(f'Row {row_index} seat {seat_index} is free')
        