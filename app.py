from fastapi import FastAPI,File,UploadFile,Request
from S3creds import client
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic_model import insertValues
from DBconnection import startDBconnection
import mysql.connector

origins = [
    "*"
]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="html")



@app.post("/Upload_Todays_Videos", response_class=HTMLResponse)
async def upload_video(request: Request,upfiles: list[UploadFile] = File(...)):
    for files in upfiles:
        content=files.file
        bucketName='batch2021'
        key=files.filename
        client.put_object(Bucket=bucketName, Key=key, Body=content)

    return templates.TemplateResponse("fileUploaded.html", {"request": request})


@app.post("/add_new_student")
async def add_new_student(studentData:list[insertValues]):
    startconnection=startDBconnection()
    cursor = startconnection.cursor()
    add_student_Query = ("INSERT INTO Students2021 "
              "(studentName, date_Of_Joining, email, PhoneNumber) "
              "VALUES (%(studentName)s, %(date_Of_Joining)s, %(email)s, %(PhoneNumber)s)")
    
    for record in studentData:
        student_data = {
        'studentName': record.name,
        'date_Of_Joining': record.date,
        'email': record.email,
        'PhoneNumber': record.phoneNum
        }
        cursor.execute(add_student_Query, student_data)
        startconnection.commit()
    
    cursor.close()
    startconnection.close()
    return "upload successful"


@app.get("/students_enrolled")
async def list_of_students_enrolled():
    startconnection=startDBconnection()
    cursor = startconnection.cursor()
    query= ("SELECT * FROM Students2021 "
         "WHERE studentID > 1")
    cursor.execute(query)
    retreived_data=[]
    for (studentID, studentName, date_Of_Joining,email,PhoneNumber,FEE_STATUS) in cursor:
        data={
            "studentID":studentID,
            "studentName":studentName,
            "date_Of_Joining":date_Of_Joining,
            "email":email,
            "PhoneNumber":PhoneNumber,
            "FEE_STATUS":FEE_STATUS
        }
        retreived_data.append(data)

    cursor.close()
    startconnection.close()
    return retreived_data


@app.put("/update_fee_status")
async def update_fee_status(studentID:list[int]):
    startconnection=startDBconnection()
    cursor = startconnection.cursor()
    query= ("update Students2021 set FEE_STATUS='PAID' where studentID=%(studentID)s")
    for id in studentID:
        data={
            "studentID":id
        }
        cursor.execute(query, data)
        startconnection.commit()
    
    cursor.close()
    startconnection.close()
    return "Succesfully updated"
    


    







