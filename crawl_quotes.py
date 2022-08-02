from bs4 import BeautifulSoup
import requests
import json


def createTotaltags(soup):
    tags = soup.find_all('div', class_='tags')
    total_tags = []
    for i in range(len(tags)):
        k = []
        for j in tags[i].find_all('a', class_="tag"):
            k.append(j.text)
        total_tags.append(",".join(k))
    return total_tags


def creatingQuotesList():
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
        authors = [author.text for author in authors]
        alltags = createTotaltags(soup)
        totalQuotes.extend(quotes)
        totalAuthor.extend(authors)
        totalTags.extend(alltags)
    data = []
    for i in range(100):
        a = {"quote": totalQuotes[i],
             "author": totalAuthor[i],
             "tags": totalTags[i].split(",")
             }
        data.append(a)
    return data, totalAuthor


def createuniqueauthorsList(totalAuthor):
    uniquelist = []
    for i in totalAuthor:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist


def createauthorlist(uniqueAuthorList):
    authors = []
    for i in uniqueAuthorList:
        i = i.replace(". ", "-")
        i = i.replace(".", "-")
        i = i.replace(" ", "-")
        i = i.replace("é", "e")
        i = i.replace("'", "")
        i = i.strip("-")
        url = "http://quotes.toscrape.com/author/"
        url = url+i+"/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        authorName = soup.find("h3", class_="author-title")
        authorName = authorName.text.strip()
        authorDateOfBirth = soup.find("span", class_="author-born-date")
        authorLocation = soup.find("span", class_="author-born-location")
        authorborn = authorDateOfBirth.text + " "+authorLocation.text
        authorDict = {"name": authorName, "born": authorborn, "reference": url}
        authors.append(authorDict)
    return(authors)


quotes, totalAuthor = creatingQuotesList()
uniqueAuthorList = createuniqueauthorsList(totalAuthor)
author = createauthorlist(uniqueAuthorList)
quotesAndAuthorsList = {"quotes": quotes, "author": author}
with open("data.json", 'w') as f:
    json.dump(quotesAndAuthorsList, f)
