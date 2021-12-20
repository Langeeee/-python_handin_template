import pandas as pd
import requests
class ex08:
    def download_cars(url):
        download = requests.get(url)
        url_content = download.content
        csv = open('cars.csv', 'wb')
        csv.write(url_content)
        csv.close()
        
        return pd.read_csv('cars.csv')