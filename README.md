# Flight Radar Europe Scrapper

It is personal project, that is focused on gathering data about flights from [Flight Radar](www.flightradar24.com)


## Table of Content

* [File Structure](#file-structure)
* [Python Dependecies](#python-dependencies)

## File Structure

```
config
├── __init__.py
└── settings.py
core
├── __init__.py
├── browser.py
├── database.py
└── logger.py
models
├── __init__.py
└── schemas.py
scrappers
├── __init__.py
└── flight_radar_scrapper.py
utils
├── __init__.py
└── parser.py
main.py
```

## Python Dependencies

* selenium: ```pip install selenium```
* BeautifulSoup4: ```pip install beautifulsoup4```
* pymongo: ```pip install pymongo```
* lxml: ```pip install lxml```
* pydantic: ```pip install pydantic```