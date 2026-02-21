import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

security_app = HTTPBasic()

class User(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

fake_users_db = {
    "saivenkat" : {
        "username" : "saivenkat",
        "name" : "Sai Venkat",
        "email" : "sai@gmail.com",
        "password" : "$2a$12$cbrHA5iY.qwpCxJVnq3afO3CPegAUlHs4CsSCyAtra2YNwyFYfo.u"
    }
}

bcrypt_lib = CryptContext(schemes=["bcrypt"])

def verify_password(input_password, db_password):
    #Use BCrypt verify method to verify if input password is matching with db password.
    return bcrypt_lib.verify(input_password, db_password)

def get_bcrypt_password(input_password):
    return bcrypt_lib.hash(input_password)


def sign_up(input_user_object: User):
    db_user_dict = {}
    db_user_dict["username"] = input_user_object.username
    db_user_dict["name"] = input_user_object.name
    db_user_dict["email"] = input_user_object.email

    hashed_password = get_bcrypt_password(input_user_object.password)
    db_user_dict["password"] = hashed_password

    fake_users_db[input_user_object.username] = db_user_dict


def authenticate_user(user_details: HTTPBasicCredentials = Depends(security_app)):
    username = user_details.username
    user = fake_users_db[username]

    if username not in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username not found, please login first."
        )
    
    # username found in db, compare the password now.
    if verify_password(user_details.password, user["password"]):
        #Login successful
        # Instead of returning username here, we should return the Token via JWT Library
        return username
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials!"
        )


# def authenticate_user(user_details: HTTPBasicCredentials = Depends(security_app)): 
#     # The userId and password we are getting in the input, compare them with the userId and password stored in the Database.
#     # for now, assume userId = "admin", password = "abcd"

#     # if user_details.username == "admin" and user_details.password == "abcd":
#     #     login successful
#     # else login failed.

#     is_username_matching = secrets.compare_digest(user_details.username, "admin")

#     is_password_matching = secrets.compare_digest(user_details.password, "abcd")

#     if is_username_matching and is_password_matching:
#         #Login Success
#         return user_details.username
    
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid credentials."
#     )
