# install python (version : 3.7+)
    # if you already have python installed, please upgrade to the latest version.
# install fastapi - pip3 install fastapi
# install pydantic - pip3 install pydantic
# install uvicorn => default server on which our FastAPI application will run.
# python -m uvicorn main:app --reload : Use this command to run the server.

# pip3 install fastapi pydantic uvicorn

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated
import json

app = FastAPI()

#ge = greater than equal
#gt = greater than
#le
#lt

class Student(BaseModel):
    id: Annotated[str, Field(..., description="student id", examples=["ST001"])]
    name: Annotated[str, Field(..., description="student name")]
    city: Annotated[str, Field(..., description="student city")]
    batch: Annotated[str, Field(..., description="student batch")]
    age: Annotated[int, Field(..., ge=18, lt=100, description="student age")] # age >= 18 & < 100
    problems_solved: Annotated[int, Field(..., description="no. of problems solved by student.")]
    passout_year: Annotated[int, Field(..., description="passout year for student.")]

    @computed_field
    @property
    def problem_solving_percentage(self) -> float:
        problem_solving_percentage = round((self.problems_solved / 150) * 100, 2)
        
        return problem_solving_percentage
        

# Home Page
@app.get("/") 
def say_hello():
    return {"message" : "Welcome to the FastAPI Class."}

@app.get("/about")
def about():
    return {"message" : "This is a sample FastAPI server"}

# this method is used to read the data from students.json file
def load_data():
    with open('students.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f)


# Create all the APIs to perform CRUD operations on Students JSON file.

# Read API - get

# get the details of all the students.
@app.get("/students")
def get_students():
    data = load_data()
    return data

# get the data for a student with the given id.
# localhost:8000/students/ST001
# student_id = Path Parameter.
# three dots inside the path function represents that student_id is a mandatory parameter.
@app.get("/students/{student_id}")
def get_student_with_id(student_id: str = Path(..., description="Pass the studentId in string format.", example="ST001")):
    file_data = load_data()

    if student_id in file_data: # valid student id.
        return file_data[student_id]
    raise HTTPException(status_code=404, detail="Student not found.")

# Implement an API to get the student details in sorted format.
# Client should be able sort students based on problems, city .....
# Client should also be able to choose among ASC or DESC
# Try to implement this api using query parameters.

# localhost:8000/sort?sort_by=<>&order=asc
# sort_by => mandatory param.
# order => optional param with default value of asc.
@app.get("/sort")
def sort_students(sort_by : str = Query(..., description="Sort on the basis of problems_solved or passout_year"), order : str = Query('asc', description="Sort in asc or desc order")):
    valid_sort_by = ['problems_solved', 'passout_year']

    # 400 status code - Bad request
    if sort_by not in valid_sort_by:
        raise HTTPException(status_code=400, detail="Students can only be sorted by problems solved or passout year.")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Order can only be either asc or desc")
    
    students_data = load_data() # Dictionary

    #sort students_data
    # if user is providing order param then use it else make it asc.
    # reverse = True => DESC
    # reverse = False => ASC
    sort_order = False
    if order == 'desc':
        sort_order = True

    sorted_students_data = sorted(students_data.values(), key=lambda x : x.get(sort_by, 0), reverse=sort_order)

    return sorted_students_data

# Create API - POST
# User should provide the student details in the request body
@app.post("/create")
def create_student(input_student_data : Student):
    # validate all the student attributes coming in the request body.

    students_data = load_data() # Dictionary

    if input_student_data.id in students_data:
        raise HTTPException(status_code=400, detail="Student with id already exists.")
    
    # Create a new student and save it in the file.
    # model_dump -> Converts Pydantic model or object into dictionary.
    input_student_dict = input_student_data.model_dump(exclude="id")

    students_data[input_student_data.id] = input_student_dict

    save_data(students_data)

    return JSONResponse(status_code=200, content='Student created successfully.')

@app.delete("/delete/{student_id}")
def delete_student(student_id : str):
    student_data = load_data()

    if student_id not in student_data:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    del student_data[student_id]

    save_data(student_data)

    return JSONResponse(status_code=200, content='Student deleted successfully.')



# {
#     "id" : "ST001",

# }

# Update API - PUT / PATCH

# Delete API - DELETE

# localhost:8000/ => say_hello function will get called.
# localhost:8000/about => about function will get called.
# localhost = 127.0.0.1


# 1234567896
# a@masai.com
# 01-01-1990

# from operator import itemgetter

# sorted(students_data.values(), key=itemgetter(sort_by), reverse=True)

# "ST001" : 

# {
#   "name": "Deepak",
#   "city": "Gurgaon",
#   "batch": "XYZ",
#   "age": 30,
#   "problems_solved": "thirty one",
#   "passout_year": 2018
# }