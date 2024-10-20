# Web Scraping Bot for Booking.com

This project is a Python-based web scraping bot that automates the process of searching hotels on Booking.com, applying filters, and retrieving results. It uses Selenium for browser automation and scrapes the hotel name, price, and rating, saving the results into a CSV file.

## Project Structure

```bash
C:Web Scraping\bot
│
├── bookings/                 # Python package for booking-related modules
│   ├── __init__.py           # Initializes the bookings package
│   ├── booking.py            # Main Booking class for browser automation
│   ├── booking_filtration.py # Class for filtering the search results
│   ├── constants.py          # Contains project constants like the BASE_URL
│   └── __pycache__/          # Compiled Python files (auto-generated)
│
├── data.csv                  # File where the scraped hotel data is saved
├── run.py                    # Main script to run the bot
└── README.md                 # Project documentation (this file)
```

### Features
  * Automated Search: The bot can automatically navigate to Booking.com and search for hotels in a specified city.
  * Filter Options: It can filter hotels based on star ratings and sort them by the lowest price.
  * Data Scraping: Scrapes hotel names, prices, and ratings and stores them in a CSV file.
  * CSV Output: The bot saves the results in data.csv for later use.

### Requirements
  * Python 3.x
  * Selenium
  * Chrome WebDriver
  * PrettyTable (for terminal table formatting)

### How It Works
  * (`booking.py`): Contains the Booking class, which extends Selenium's Chrome WebDriver. It handles the entire automation process such as navigating to the site, selecting currency, choosing destination, check-in/check-out dates, number of guests, and filtering the results.
  * (`booking_filtration.py`): This class is responsible for applying filters like star ratings and sorting by price.
  * (`run.py`): The entry point to run the bot. This script interacts with the Booking class to perform the hotel search and scrape results.

### Customization
You can easily customize the following parameters in (`run.py`):

  * Destination City: Change the select_destination() parameter to your desired city.
  * Check-in/Check-out Dates: Modify the checkin_checkout() method to specify the dates of your stay.
  * Number of Guests: Adjust the no_guest() method to set the number of guests for the search.

## Output

The results are saved in a CSV file (`data.csv`) with the following format:

| Hotel Name     | Hotel Price | Hotel Score |
|----------------|-------------|-------------|
| Hotel ABC      | ₹5000       | 8.9         |
| Hotel XYZ      | ₹4500       | 8.4         |
| ...            | ...         | ...         |
The results are displayed in Command Line Interface(CLI) with the following format:
<br>
<img src="https://github.com/user-attachments/assets/e9a3c1f3-0b78-4591-8693-b75455f79405" width="300" height="150" />
