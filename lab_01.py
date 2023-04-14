# create a board program

import datetime

class Post:
    def __init__(self, title, content, author):
        self._id = id(self)
        self.title = title
        self.content = content
        self.author = author
        self.comments = []
        self.date = datetime.datetime.now()

    def add_comments(self, comment):
        self.comments.append((comment, datetime.datetime.now()))

    def get_comments(self):
        return self.comments

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\nDate: {self.date}"

class Board:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_post(self, post_id):
        for post in self.posts:
            if post._id == post_id:
                return post
        return None

    def __str__(self):
        return f"Board: {self.name}\nNumber of Posts: {len(self.posts)}"

# 2. QnA Board, free Board 객체 생성

qna = Board('QnA Board')
free = Board('free Board')


q1 = Post('객체지향 원리', '홍길동','객체지향의 핵심 원리 중 추상화에 대해 구체적인 예를 들어 설명해 주세요.')
q2 = Post('파이썬 언어', '홍길순', '파이썬 언어가 다른 프로그래밍 언어에 비해 보편화된 이유가 무엇인가요?')

qna.add_post(q1)
qna.add_post(q2)

for post in qna.posts:
    print(post, '\n')
