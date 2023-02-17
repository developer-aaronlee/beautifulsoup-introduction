from bs4 import BeautifulSoup
import requests
# import lxml

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.text)
# print(soup.title.string)
# print(soup.prettify())

# a_tags = soup.find_all(name="a")
# print(a_tags)

# for x in a_tags:
    # print(x.getText())
    # print(x.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)


response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")
# print(soup.title)

article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
# print(article_text)
# print(article_link)

article_upvote = soup.find(name="span", class_="score")
# print(article_upvote.getText().strip(" points"))

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for x in articles:
    article_texts.append(x.getText())
    article_links.append(x.get("href"))
# print(article_texts)
# print(article_links)

# article_upvotes = [int(x.getText().split()[0]) for x in soup.find_all(name="span", class_="score")]
article_upvotes = [int(x.getText().strip(" points")) for x in soup.find_all(name="span", class_="score")]
# print(article_upvotes)

most_upvotes = max(article_upvotes)
most_upvotes_index = article_upvotes.index(most_upvotes)
most_upvotes_article = article_texts[most_upvotes_index]
most_upvotes_link = article_links[most_upvotes_index]
print(most_upvotes_article)
print(most_upvotes_link)
print(most_upvotes)



