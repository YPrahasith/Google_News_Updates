import sqlite3
import time
from bs4 import BeautifulSoup
import requests

headlines = []
url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'
page = requests.get(url)

#create a data structure
conn = sqlite3.connect('GNews.db')
c = conn.cursor()

#Create table
c.execute('''Create TABLE if not exists Gnews("Headlines")''')

try:
    while True:
        soup = BeautifulSoup(page.text, "html.parser")
        links=soup.find_all('a',attrs={'class':'DY5T1d RZIKme'})
        for j in links:
            if j not in headlines:
                headlines.append(j.text)
        
        #print(headlines)
        time.sleep(900)

except:
    #Insert links into table
    for item in headlines:
        c.execute("INSERT INTO GNews(Headlines) VALUES(?)", (item,))
        conn.commit()
    #query database
    c.execute("SELECT * FROM GNews")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()