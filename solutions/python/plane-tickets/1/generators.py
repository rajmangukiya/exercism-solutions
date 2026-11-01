"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    seats = ["A", "B", "C", "D"]
    
    for seat_number in range(number):
        seat_index = seat_number % len(seats)

        yield seats[seat_index]

    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    columns = ["A", "B", "C", "D"]
    row = 0
    column = 0
    
    for seat_index in range(number):
        if row == 12:
            row = 13

        yield str(row + 1) + columns[column]
        if (column == len(columns) - 1):
            column = 0
            row += 1
        else:
            column += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    dict = {}

    get_seat = generate_seats(len(passengers))

    for passenger in passengers:
        dict[passenger] = next(get_seat)

    return dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    code_length = 12

    for seat_number in seat_numbers:
        partial_code = seat_number + flight_id
        zeros = "0" * (code_length - len(partial_code))

        yield partial_code + zeros
