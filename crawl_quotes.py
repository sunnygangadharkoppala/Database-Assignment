from bs4 import BeautifulSoup
import requests
totalQuotes = []
totalAuthor = []
totalTags = []
for i in range(1, 11):
    url = "https://quotes.toscrape.com/page/"
    url = url+str(i)+"/"
    response = requests.get(url)
    response.status_code
    soup = BeautifulSoup(response.content, 'lxml')
    quotes = soup.find_all("span", class_='text')
    quotes = [quote.text[1:-1] for quote in quotes]
    authors = soup.find_all("small", class_="author")
    authors = [author.text[1:-1] for author in authors]
    tags = soup.find_all('div', class_='tags')
    total_tags = []
    for i in range(len(tags)):
        k = []
        for j in tags[i].find_all('a', class_="tag"):
            k.append(j.text)
        total_tags.append(",".join(k))
    totalQuotes.extend(quotes)
    totalAuthor.extend(authors)
    totalTags.extend(total_tags)


quotes_file = {"quotes": totalQuotes,
               "author": totalAuthor, "tags": totalTags}
print(quotes_file)
