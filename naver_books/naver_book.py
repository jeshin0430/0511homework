def extract_info(book_list):
    result = []
    for book in book_list:
        title = book.find("dt").find("a").string
        img_src = book.find("div", {"class" : "thumb_type thumb_type2"}).find("img")["src"]
        detail_link = book.find("div", {"class" : "thumb_type thumb_type2"}).find("a")["href"]
        writer = book.find("dd", {"class": "txt_block"}).find("a").string
        publisher = book.find("dd", {"class": "txt_block"}).find("a", {"class":"N=a:bta.publisher"}).string
        
        book_info = {
            "title" : title,
            "img_src" : img_src,
            "detail_link" : detail_link,
            "writer" : writer,
            "publisher" : publisher,
        }
        result.append(book_info)
    return result
    print(result)