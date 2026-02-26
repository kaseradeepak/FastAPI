from tables import create_tables
from crud_operations import create_users, create_posts, get_user_by_id, get_all_users, update_user_name, delete_user_by_id, get_posts_with_author_name, get_post_count_per_user

create_tables()

# create_users('Anubha', 'anubha@amazon.com', 'ksdfj')
# create_users('Anjum', 'anjum@amazon.com', ';jfklsdjf')
# create_users('Murali', 'murali@amazon.com', 'sdfjklsdjfklds')
# create_posts('1', 'Hi, I am Anubha and this is my first post.')
# create_posts('2', 'Hi, I am Anjum and this is my first post.')
# create_posts('3', 'Hi, I am Murali and this is my first post.')

# create_posts('3', 'Hi Everyone.')
# create_posts('3', 'Hey Everyone.')
# create_posts('2', 'Hello World!')



# print(get_user_by_id(2))
# print(get_all_users())

# update_user_name(2, 'Anubha Sharma')
# update_user_name(1, 'Sunny')

# delete_user_by_id(1)

# print(get_posts_with_author_name())

# print(get_post_count_per_user())
