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
