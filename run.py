from scraper import GoogleMapsScraper
from config import HEADERS

searchtext = input('Enter the place to search: ').replace(' ', '+')
querylen = int(input('Enter the number of result(s): '))
filename = input('Enter the filename: ')

with GoogleMapsScraper(debug=True) as bot:
    bot.search_query(searchtext)
    bot.write_data(HEADERS, filename)
    url = bot.identify_url()
    if url == 'place':
        bot.get_place_data(filename)
    elif url == 'search':
        bot.get_places_data(filename, querylen)
