from bookings.booking import Booking
import time
with Booking() as bot:
    bot.land_first_page()
    # bot.currency_selector()
    bot.select_destination('Hyderabad')
    bot.checkin_checkout(checkin_date='2024-10-21',checkout_date='2024-10-24')
    bot.no_guest(4)
    bot.click_search()
    bot.apply_filtration()