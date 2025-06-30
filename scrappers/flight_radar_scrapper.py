import datetime

from utils import parser, helpers
from models.schemas import Flight
from core import logger


scrapper_logger = logger.init_logger('flight_radar')


def scrape(URL: str, departure: bool):
    flights = []
    
    soup = parser.parse_HTML(URL)
    
    if soup:
        header = soup.find('header')
        airport = ''
        
        if header:
            h2 = header.find('h2').text[1:4]

            if h2:
                airport = h2
            else:
                scrapper_logger.error(f"Coulnd't find element <h2> url: { URL }")
        else:
            scrapper_logger.error(f"Couldn't find element <header> url: { URL }")
            
        tbody = soup.find('tbody')
        
        if tbody:
            table_rows = tbody.find_all('tr', attrs= {
                'data-date': datetime.now().strftime('%A, %b %d')  ### REFACTOR INTO UTILS
            })
            
            if table_rows:
                for tr in table_rows:
                    flight = Flight()
                    
                    
            else:
                scrapper_logger.error(f"Couldn't find element <tr> url: { URL }")
        
        else:
            scrapper_logger.error(f"Couldn't find element <tbody> url: { URL }")