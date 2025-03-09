from fastapi import FastAPI

app=FastAPI() #creating an instance of FastAPI

@app.get("/") #creating a route
def hoome():
    return "Home Page"

@app.get("/json") #creating a route
def json_data():
    return {"data": " FastAPI is cool"}

@app.get("/about")
def about_page():
    return {"about": "This is a about page"}

# Path Parameters
@app.get('/blogs')
def get_blogs():
    return {"data" :[{"blogs": "1"}, {"blogs": "2"}]}

@app.get('/blogs/{id}')
def get_id(id:int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def get_comments(id:int):
    return {"data": id}

# always keep the dyanmic routes at the end of the static routes