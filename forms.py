from typing import Optional

from fastapi import Request

# perubahan form
class UserCreateQA:
    def __init__(self, request: Request):
        self.request: Request = request
        self.context: Optional[str] = None
        self.question: Optional[str] = None
    
    def load_data(self):
        form = self.request.form()
        self.context = form.get("context")
        self.question = form.get("question")

        return [self.context, self.question]