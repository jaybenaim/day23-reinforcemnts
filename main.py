seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None,  "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]
def check_seat(classroom): 
	seat_available = classroom
	for row_index, row in enumerate(classroom):  
		row_index += 1 
		for seat_index, seat in enumerate(row): 
			seat_index += 1
			if seat == None: 
				print(f'Row {row_index} seat {seat_index} is free') 
				confirm = input('Would you like to sit here? (y/n)\t')

				if confirm == 'y': 
					name = input('Please enter your name.\n')
					seat_available[row_index-1 ][seat_index-1] = name 

					print(seat_available)
					exit() 







  

            
        
check_seat(seats) 
