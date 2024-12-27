# Lycinema - Ticket Booking

## Overview
This program is a ticket booking system that allows users to book tickets for movies, view their booked tickets, cancel tickets, and browse available movies. Follow the instructions below to use the system effectively.

---

## How to Use the Program

### 1. **Launch the Program**
Run the lycinema.py in a Python environment to start the ticket booking system. The main menu will be displayed with the following options:

```
1. Book a ticket
2. View your ticket
3. Cancel ticket
4. View Available Movies
5. Exit
```

### 2. **Booking a Ticket**
- Select option `1` from the main menu.
- A list of available movies will be displayed. Choose a movie by entering its ID.
- Select a cinema by entering its ID.
- Choose your seat by entering the desired column and row.
  - Columns are vertical (0-4).
  - Rows are horizontal (0-9).
- If the seat is available, the ticket will be booked successfully.
- If the seat is occupied or invalid inputs are provided, the system will prompt you to try again.

### 3. **View Your Ticket**
- Select option `2` from the main menu.
- Enter your ticket ID to view your ticket details.
- The system will display the ticket details, such as movie name, cinema, and seat information.

### 4. **Cancel a Ticket**
- Select option `3` from the main menu.
- Enter your ticket ID to cancel the ticket.
- The system will confirm whether the ticket was successfully canceled.

### 5. **View Available Movies**
- Select option `4` from the main menu.
- The system will display a list of all available movies.

### 6. **Exit the Program**
- Select option `5` from the main menu to exit the program.

---

## Notes
- Ensure the terminal is cleared when navigating between options for better readability.
- Input validation is performed, so follow the prompts carefully to avoid errors.
- If you encounter an issue, restart the program and try again.

