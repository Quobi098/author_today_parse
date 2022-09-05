import csv
from bs4 import BeautifulSoup as BS
import lxml
import requests

page = 1

#Сохраняем страницы как файлы.
# while True:
#     r = requests.get('https://author.today/work/genre/all?eg=-&fnd=false&page=' + str(page))
#     html = BS(r.content, 'lxml')
#     items = html.select('div.book-row-content')
#
#     with open(f'files/author_today_page_{page}.html', 'w', encoding='utf8') as file:
#         file.write(r.text)
#
#     if (len(items)):
#         page += 1
#     else:
#         break


#Работа с файлами
while True:
    with open(f'files/author_today_page_{page}.html', encoding='utf8') as file:
        src = file.read()

    soup = BS(src, 'lxml')
    items = soup.select('div.book-row-content')

    if(len(items)):
        for el in items:
            book_name = el.find(class_='book-title').text.strip()
            book_author = el.find(class_='book-author').text.strip()
            book_rate = el.find(class_='book-stats').find_all('span')[1].text.strip()
            book_views = el.find(class_='book-stats').find_all('span')[0].text.strip()
            book_genre = el.find(class_='book-genres').text.strip()
            book_description = el.find(class_='annotation').text.strip()


            with open('Author_Today_Books.csv', 'a', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        book_name,
                        book_author,
                        book_rate,
                        book_views,
                        book_genre,
                        book_description
                    )
                )

            page += 1
    else:
        break