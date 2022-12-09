from booking.booking import Booking
import time
import datetime

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='KGS')
    bot.select_place_to_go('New York')
    first_date = datetime.date.today() + datetime.timedelta(days=10)
    second_date = first_date + datetime.timedelta(days=15)
    bot.select_dates(check_in_date=f'{first_date}', check_out_date=f'{second_date}')
    bot.select_adults(6)
    bot.click_search()
    bot.apply_filtrations()
    time.sleep(5)
    print('Exiting...')