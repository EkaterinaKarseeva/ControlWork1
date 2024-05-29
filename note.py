import json
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.id = int(datetime.now().timestamp())  # уникальный идентификатор на основе текущего времени
        self.title = title
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
        }
