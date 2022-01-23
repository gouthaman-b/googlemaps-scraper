# Google Maps Scraper
A web scraper written in  Python using Selenium Library, this script allows
to scrape data from google maps.
And the data is written in csv file format.

# Requirements
- Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html).
- python 3.8 or above
- selenium 4.1.0

# Usage
After installing all the requirements, change the value of EXE_PATH in [config.py](https://github.com/kryo-x/googlemaps-scraper/blob/main/config.py)
```
python run.py
```

* `place`
  * Place to search in google maps.
* `querylen`
  * Number of results required.
* `filename`
  * Filename to save the result.

## Example
```
python run.py
Enter the place to search: hotels near <place>
Enter the number of result(s): 10
Enter the filename: test1.csv
```
see the result in [example](https://github.com/kryo-x/googlemaps-scraper/blob/main/example/example.csv)

# To-do
- To scrape lat/long from pluscode.
- To create a cli.
