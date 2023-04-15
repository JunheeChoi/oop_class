
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self._id = id(self)
        self._title = title
        self._content = content
        self._author = author
        self._comments = []
        self._date = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def author(self):
        return self._author

    @property
    def date(self):
        return self._date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def comments(self):
        return self._comments

    def add_comment(self, comment):
        comment.date = datetime.now()
        self._comments.append(comment)

    def __str__(self):
        return f"[{self.id}] {self.title}\n{self.author} | {self.date}\n{self.content}"

    def search(self, keyword):
        if keyword in self.title:
            return self.id
        else:
            return None


class QnA_Board:
    id = 0
    no_posts = 0

    def __init__(self, name: str):
        self._name = name
        self._posts = []

    @property
    def name(self):
        return self._name

    @property
    def posts(self):
        return self._posts

    @posts.setter
    def posts(self, new_posts):
        self._posts = new_posts

    def add_post(self, title: str, content: str, author: str):
        post = Post(title, content, author)
        self._posts.append(post)
        QnA_Board.id += 1
        QnA_Board.no_posts += 1

    def get_post(self, post_id: int):
        for post in self._posts:
            if post.id == post_id:
                return post
        return None

    def remove_post(self, post_id: int):
        for i, post in enumerate(self._posts):
            if post.id == post_id:
                del self._posts[i]
                QnA_Board.no_posts -= 1
                return True
        return False

qna = QnA_Board('질의,응답 게시판')

p1 = Post('객체지향 원리', '객체지향의 핵심 원리 중 추상화에 대해 구체적인 예를 들어 설명해주세요.', '홍길동')
p2 = Post('파이썬 언어', '파이썬 언어가 다른 프로그래밍 언어에 비해 보편화된 이유가 무엇인가요?', '홍길순')

qna.add_post(p1.title, p1.content, p1.author)
qna.add_post(p2.title, p2.content, p2.author)

for post in qna.posts:
    if post.title == '파이썬 언어':
        qna.remove_post(post.id)
        break

for post in qna.posts:
    print(post, '\n')
