from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hoome():
    return "Home Page"

print("Hello World")