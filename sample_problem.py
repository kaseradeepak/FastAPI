from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
# pip3 install python-jose
from jose import jwt

app = FastAPI()

ALGORITHM = "HS256"
SECRET_KEY = "our_secret_key"

class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    WORKER = "worker"

class User(BaseModel):
    username: str
    password: str
    role: Role

users_db = {
    "anjum" : {"username" : "anjum", "password" : "abcd", "role" : Role.ADMIN},
    "anubha" : {"username" : "anubha", "password" : "pqrs", "role" : Role.MANAGER},
    "neeraj" : {"username" : "neeraj", "password" : "1234", "role" : Role.WORKER}
}


#JWT => a.b.c
# a : algorithm
# b : payload
# c : signature
# data = { "username" : "anjum", "role" : "admin"}
def create_access_token(data: dict):
    # Creates a JWT Token for the username and role coming in the input param
    
    # token will be valid for 60 mins after creation.
    token_expiry_time = datetime.utcnow() + timedelta(minutes=60)
    data.update("expiry", token_expiry_time)
    # data = { "username" : "anjum", "role" : "admin", "expiry" : "21st Feb 2026, 9:24 PM"}

    # The below line will create the token in the form a.b.c 
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    
    return token

#post -> Create
#login -> verifies the credentials and generates the token.
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user: 
        # user doesn't exist.
        raise HTTPException(status_code=401, detail="User not found, please sign-up first.")
    
    #Username is present in the database, now check the password.
    if user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Unauthorized error, wrong password.")

    #Login successfull -> create access token.
    access_token = create_access_token(
        data = {"username" : user['username'], "role" : user['role']}
    )

    return access_token
