from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{
        'name':'surya',
        'age':19,
        'subject':'B.C.A'
        }
    }

@app.get('/about')
def about():
    return 'this is about page'

@app.get('/contact')
def contact():
    return {
        'data' : {
            'status':'about'
        }
    }

