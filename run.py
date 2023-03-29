# from app import app
from app import create_app
app= create_app()
#set flask app run in debug mode
if __name__== '__main__':
    app.run(debug=True)
