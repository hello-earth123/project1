import json


def best_new_books(books):
    # 여기에 코드를 작성합니다.
    pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    print(best_new_books(books))
