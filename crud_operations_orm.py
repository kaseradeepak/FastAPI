from models_orm import User, Post
from db_orm import orm_session

def create_user(input_name: str, input_email: str):
    with orm_session() as session:
        user = User(name = input_name, email = input_email)
        session.add(user)
        session.commit()

def create_post(input_user_id: int, input_content: str):
    with orm_session() as session:
        post = Post(user_id = input_user_id, content = input_content)
        session.add(post)
        session.commit()
