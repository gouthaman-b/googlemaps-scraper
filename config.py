# path of the chromedriver
EXE_PATH = r'path/to/chromedriver'

LOGFILE = 'scraper.log'

URL = 'http://www.google.com/maps/search/'
HEADERS = [
    'PlaceName', 'PlaceRating', 'PlaceReviews', 'PlaceAddress',
    'PlaceContact', 'PlaceWebsite', 'PlacePlusCode', 'PlaceURL'
]

WAIT_TIME = 3
TIMEOUT = 2

# xpath of web elements
PLACE_NAME_XPATH = '//*[@id="pane"]/div/div[1]/div/div/div[2]/' \
    'div[1]/div[1]/div[1]/h1/span[1]'
PLACE_RATING_XPATH = '//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]/' \
    'div[1]/div[2]/div/div[1]/div[2]/span/span/span'
PLACE_REVIEWS_XPATH = '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/' \
    'div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button'
PLACE_ADDRESS_SRC = 'place_gm_blue_24dp'
PLACE_CONTACT_SRC = 'phone_gm_blue_24dp'
PLACE_WEBSITE_SRC = 'public_gm_blue_24dp'
PLACE_PLUSCODE_SRC = 'ic_plus_code'

FIRST_RESULT_XPATH = '//*[@id="pane"]/div/div[1]/div/div/div[last()]/' \
    'div[1]/div[5]/div/a'
BOTTOM_PANE_XPATH = '/html/body/div[3]/div[9]/div[23]/div[2]/div/div[1]/' \
    'div/div[1]/div/div/div/div[2]/div[2]/div'
NEXT_PAGE_XPATH = '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/' \
    'div[last()]/div[2]/div/div[1]/div/button[2]'
BACK_BUTTON_XPATH = '//*[@id="omnibox-singlebox"]/div[1]/div[1]/button'
