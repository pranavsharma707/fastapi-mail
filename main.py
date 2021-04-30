from fastapi import FastAPI,BackgroundTasks,File,Form,UploadFile
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import ValidationError
from typing import List
import schema
app = FastAPI()



conf = ConnectionConfig(
    MAIL_USERNAME = "javashrm@gmail.com",
    MAIL_PASSWORD = "corejava@1234",
    MAIL_FROM = "javashrm@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    #MAIL_FROM_NAME="pranav",
    MAIL_TLS = True,
    MAIL_SSL = False,
)

@app.post("/send_mail")
async def send_mail(email:schema.Email)->JSONResponse:

  
    template = """
        <html>
        <body>
          
    <p>Hi !!!
        <br>Thanks for using fastapi mail, keep using it..!!!</p>
  
        </body>
        </html>
        """
  
    message = MessageSchema(
        subject=email.dict().get('subject'),
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=template,
        subtype=email.dict().get('topic'),
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    print(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})