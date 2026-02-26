from db import engine
from tables import users, posts
from sqlalchemy import insert, select, update, delete, func

# Create
def create_users(input_name: str, input_email: str, input_address: str):
    with engine.connect() as conn:
        # insert into users(name, email) values ('Murali', 'murali@amazon.com')
        statement = insert(users).values(name=input_name, email=input_email, address=input_address)
        conn.execute(statement)
        conn.commit() # commit is also required for Write Queries.

def create_posts(user_id: int, content: str):
    with engine.connect() as conn:
        # insert into users(name, email) values ('Murali', 'murali@amazon.com')
        statement = insert(posts).values(user_id=user_id, content=content)
        conn.execute(statement)
        conn.commit() # commit is also required for Write Queries.

#Read
def get_user_by_id(input_id: int):
    with engine.connect() as conn:
        query = select(users).where(users.c.id == input_id)
        result = conn.execute(query).first()
        return result

def get_all_users():
    with engine.connect() as conn:
        query = select(users) # select * from users.
        result = conn.execute(query).fetchall()
        return result

# Write a function to get the posts for a user_id.

# Update
def update_user_name(user_id: int, new_name: str):
    with  engine.connect() as conn:
        # update users set name = new_name where id = user_id
        query = update(users).where(users.c.id == user_id).values(name=new_name)
        conn.execute(query)
        conn.commit()

# Delete
def delete_user_by_id(user_id: int):
    with  engine.connect() as conn:
        # delete from users where id = user_id
        query = delete(users).where(users.c.id == user_id)
        conn.execute(query)
        conn.commit()

# Join users and posts.
# Get all the posts with their author names.
# select p.id, p.content, u.name from users u join posts p on u.id = p.user_id
def get_posts_with_author_name():
    with engine.connect() as conn:
        query = select(
            posts.c.id,
            posts.c.content,
            users.c.name
        ).join(users, posts.c.user_id == users.c.id)

        result = conn.execute(query).fetchall()
        return result

# get the count of posts for each user.
def get_post_count_per_user():
    with engine.connect() as conn:
        # select user_id, count(id) from posts group by id;
        query = select(posts.c.user_id, func.count(posts.c.id)).group_by(posts.c.user_id)
        result = conn.execute(query).fetchall()
        return result
