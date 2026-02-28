from models_orm import User, Post
from db_orm import orm_session

# Create
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

# Read
def get_user_by_id(input_user_id: int):
    with orm_session() as session:
        user = session.get_one(User, input_user_id) # select * from user where id = input_user_id
        return user

# get all the posts by user_id
def get_all_posts_by_user_id(input_user_id: int):
    with orm_session() as session:
        user = session.get_one(User, input_user_id) # Lazy -> this query will only fetch the user object form users table.
        if user:
            posts = user.posts # This will make another query to the posts table to get the posts made by the user. 
            return posts
        return []