from datetime import datetime

class Note:
    def __init__(self, title, content, id=None, created_at=None):
        self.id = id if id else int(datetime.now().timestamp())
        self.title = title
        self.content = content
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
        }
