import requests
from bs4 import BeautifulSoup
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(database="mad", user="postgres", password="1234", host="127.0.0.1", port="5432")
cur = conn.cursor()

# URL of the Amazon product page for iPhone 12
url = ""

# Send a GET request to the URL and get the HTML response
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Find all the customer reviews on the page
reviews = soup.find_all("div", {"data-hook": "review"})

# Loop through each customer review and extract its details
for review in reviews:
    title = review.find("a", {"data-hook": "review-title"}).text.strip()
    text = review.find("span", {"data-hook": "review-body"}).text.strip()
    style_name = review.find("a", {"data-hook": "format-strip"}).text.strip()
    color = style_name.split(" - ")[0]
    verified_purchase = review.find("span", {"data-hook": "avp-badge"}).text.strip()
    
    # Insert the extracted details into the PostgreSQL database
    cur.execute("INSERT INTO iphone_reviews (title, text, style_name, color, verified_purchase) VALUES (%s, %s, %s, %s, %s)", (title, text, style_name, color, verified_purchase))
    
# Commit the changes to the database and close the cursor and connection
conn.commit()
cur.close()
conn.close()
