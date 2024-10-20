from bookings.booking import Booking
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.currency_selector()
        bot.select_destination('Hyderabad')
        bot.checkin_checkout(checkin_date='2024-10-21',checkout_date='2024-10-24')
        bot.no_guest(4)
        bot.click_search()
        bot.apply_filtration()
        bot.report_results()
except Exception as e:
    if 'in PATH' in e:
        print(
            'You are trying to run bot from the command line\n'
            'Please add to PATH your Selenium Drivers\n'
            'Windows: \n'
            'set PATH=%PATH%,C:path-to-your-selenium-drivers-folder \n\n'
            )
    else:
        print(f"Exception {e}")
