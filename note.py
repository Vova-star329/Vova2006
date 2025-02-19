class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"