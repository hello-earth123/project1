import json
from pprint import pprint


# 여기에 코드를 작성합니다.
# 데이터 추출해야 하는 항목
# 데이터 수집, 데이터 변환
# def books_info(books, categories):
    
def books_info(books, categories):

    # categories 변수에는 카테고리가 dictionary의 리스트로 되어 있음.
    """
    >>> categories_list
    [{'id': 31916, 'name': '과학'}, {'id': 31908, 'name': '에세이 / 수필'}, {'id': 151138, 'name': '자기계발'}, {'id': 153690, 'name': '서양철학'}, {'id': 151128, 'name': '문학'}, {'id': 50919, 'name': '영미소설'}, {'id': 89481, 'name': '외국 과학소설'}, {'id': 50922, 'name': '독일소설'}, {'id': 70216, 'name': '성공학'}, {'id': 51786, 'name': '육아 일반'}, {'id': 51082, 'name': '건축'}, {'id': 51381, 'name': '인문'}, {'id': 51260, 'name': '프랑스 문학'}, {'id': 50982, 'name': '미술사'}, {'id': 51545, 'name': '인류학'}, {'id': 51205, 'name': '생명과학'}, {'id': 51310, 'name': '우주과학'}, {'id': 50921, 'name': '철학'}, {'id': 51449, 'name': '윤리학'}, {'id': 2721, 'name': '컴퓨터 공학'}]
    => 만약에 특정 id에 일치하는 name을 찾으려면, 이 리스트를 전부 일일이 돌면서 하나씩 찾아봐야 함 (비효율적)

    >>> category_dict
    {31916: '과학', 31908: '에세이 / 수필', 151138: '자기계발', 153690: '서양철학', 151128: '문학', 50919: ' 영미소설', 89481: '외국 과학소설', 50922: '독일소설', 70216: '성공학', 51786: '육아 일반', 51082: '건축', 51381: '인문', 51260: '프랑스 문학', 50982: '미술사', 51545: '인류학', 51205: '생명과학', 51310: '우주과학', 50921: '철학', 51449: '윤리학', 2721: '컴퓨터 공학'}
    => 만약 특정 id에 해당하는 name을 찾으려면 dict에 id를 집어넣으면 바로 나옴
    ex) category_dict[31916] = 과학

    """
    category_dict = {} # 빈 딕셔너리 만들기
    for category in categories: # category 예시 : {'id': 151128, 'name': '문학'}
        category_dict[category['id']] = category['name']


    new_books = [] # books => new_books
    books_data = []
        
    for book in books: # 원래 책 리스트에서 book을 하나씩 꺼내서
        category_ids = book['categoryId'] # [151128, 50919]
        category_names = [category_dict[category_id] for category_id in category_ids]

        # print(category_ids)
        # print(category_names)

        book['categoryName'] = category_names # book을 수정하고 

        new_books.append(book) # 수정한 book을 새로운 빈 리스트에 집어넣는다.
        
    
        new_data = {
        'author' : book.get('author'),
        'categoryName' : book.get('categoryName'),
        'cover' : book.get('cover'),
        'description' : book.get('description'),
        'id' : book.get('id'),
        'priceSales' : book.get('priceSales'),
        'title' : book.get('title')
            }
        books_data.append(new_data)
    return books_data

book_list = []
review_rank = []
def best_book(books):
    for rank in book_list:
        review_rank.append(rank["customerReviewRank"])
    max_review_book = max(review_rank)  # 9.9
    
    for rank in book_list:
        if rank["customerReviewRank"] == max_review_book:
            max_book = rank["title"]
            
    return max_book

 
book_2023 = []
def new_books(books):
    for year in book_list:
        if '2023' in year['pubDate']:
            book_2023.append(year['title'])
            
    return book_2023  






    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding='utf-8'
    )
    categories_list = json.load(categories_json)
    
    books_dir = current_dir / 'data' / 'books' 
    
    for json_file in books_dir.glob('*.json'):
        with open(json_file, encoding='utf-8') as f:
            book_data = json.load(f)
            book_list.append(book_data)

    pprint(books_info(books, categories_list))
    pprint(best_book(book_data))
    print(new_books(books))





# 리스트 컴프리헨션
# - 리스트를 한줄로 만드는 방법
# -  [표현식 for 항목 in 반복가능한객체 if 조건]