# Google_News_Updates
Simple Python Script to fetch headlines using beautiful soup from Google News and display the same in a python-sqlite3 database

### Dependencies Required
1. BeautifulSoup
2. Requests
3. Sqlite3

### How does it Work
With the aid of Beautiful Soup it parses the HTML content and selectively extracts the Headlines. The headlines are extracted once in every 15 minutes in an infinite loop in the try block, and once the execution of the try block is interrupted, it adds all the distinct headlines to the python sqlite3 database and commits the same.

### How to Run the Code
py Gnews_Headlines.py