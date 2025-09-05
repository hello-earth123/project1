import json
from pprint import pprint


def book_info(book):
    pass
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    book_json = open(current_dir / 'data' / 'book.json', encoding="utf-8")
    book = json.load(book_json)

    pprint(book_info(book))
