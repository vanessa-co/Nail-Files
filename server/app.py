from flask import request, make_response, session
from flask_restful import Resource
from config import app, db, api
#from models import Order, PotatoDish, DishOrder, User
from flask_cors import CORS
from flask_session import Session
CORS(app, supports_credentials=True, allow_headers=['Content-Type', 'session'])
Session(app)
app.secret_key = b'\x9d\xe0\x0e\t2\xd7s\x0c\xcc&\xe8\x84'


@app.route('/')
def index():
    return 'Hello, world'



if __name__ == '__main__':
    app.run(port=5555)
