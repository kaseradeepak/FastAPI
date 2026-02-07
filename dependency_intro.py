from fastapi import FastAPI, Depends
from user_details import get_user_details

app = FastAPI()


@app.get("/profile")
def get_profile_info(user = Depends(get_user_details)):
    #Here we need to get the user details from get_user_details function.
    return user