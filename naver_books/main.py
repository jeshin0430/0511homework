import requests
from bs4 import BeautifulSoup
from naver_book import extract_info
import csv

file = open("books.csv", mode="w", newline ='')
writer = csv.writer(file)
writer.writerow(["title", "img_src", "detail_link", "writer", "publisher"])

final_result = []

for i in range(8):
    print(f'{i+2}번째 페이지 크롤링 중...')
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+2}')
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol", {"class" : "basic"})
    book_list = book_list_box.find_all("li")
    final_result = final_result + extract_info(book_list)
print(final_result)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["img_src"])
    row.append(result["detail_link"])
    row.append(result["writer"])
    row.append(result["publisher"])

    writer.writerow(row)