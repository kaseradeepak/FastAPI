import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security_app = HTTPBasic()

def authenticate_user(user_details: HTTPBasicCredentials = Depends(security_app)): 
    # The userId and password we are getting in the input, compare them with the userId and password stored in the Database.
    # for now, assume userId = "admin", password = "abcd"

    # if user_details.username == "admin" and user_details.password == "abcd":
    #     login successful
    # else login failed.

    is_username_matching = secrets.compare_digest(user_details.username, "admin")

    is_password_matching = secrets.compare_digest(user_details.password, "abcd")

    if is_username_matching and is_password_matching:
        #Login Success
        return user_details.username
    
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
        detail="Invalid credentials."
    )
