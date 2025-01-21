from flask import Flask, request , render_template

books = [
        {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
        {"id": 2, "year": 1925},
        {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949}, 
        {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}, 
        {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
        ]

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
     return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
     nom = request.form.get('Nom')
     motDePasse = request.form.get('motdepasse')
     return f'Nom : {nom}/ Mot de passe :{motDePasse}'


@app.route('/add', methods=["POST"])
def Add():
     id = len(books)+ 1
     title = request.form.get('title')
     author = request.form.get('author')
     year = request.form.get('year')
     
     books.append(
          {f'id : {id}/ title:{title}/ author:{author}/ year :{year}'}
    )
     
     return f' titre:{title} | author:{author} | year :{year}'
     

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8080)