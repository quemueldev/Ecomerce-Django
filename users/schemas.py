from ninja import Schema

class SignUpSchema(Schema):
    email:str
    name:str
    password: str

class SignInSchema(Schema):
    email:str
    password: str

class SendSchema(Schema):
    email: str

class VerifySchema(Schema):
    email: str
    code:str

class EmailSchema(Schema):
    email:str
