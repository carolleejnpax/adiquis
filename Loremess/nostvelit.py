from bs4 import BeautifulSoup

# Assuming 'text' contains the HTML content
text = BeautifulSoup(text, 'lxml').get_text()
