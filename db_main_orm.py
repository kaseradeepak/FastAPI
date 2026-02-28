from models_orm import create_tables
from crud_operations_orm import create_user, create_post, get_user_by_id, get_all_posts_by_user_id

# create_tables()

# create_user('Murali', 'murali@amazon.com')
# create_user('Sweta', 'sweta@google.com')
# create_user('Anubha', 'anubha@meta.com')

# create_post('1', 'Hi, I am Murali')
# create_post('1', 'Hi, I am Murali 2')
# create_post('2', 'Hi, I am Sweta')
# create_post('3', 'Hi, I am Anubha')
# create_post('3', 'Hi, I am Anubha-2')
# create_post('3', 'Hi, I am Anubha-3')

print(get_all_posts_by_user_id(1)) # Lazy

# posts = get_all_posts_by_user_id(2)
# print(posts)