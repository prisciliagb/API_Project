from flask import Flask, request , render_template
books = [
        {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
        {"id": 2, "year": 1925},
        {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949}, 
        {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}, 
        {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
        ]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/search' , methods=['GET'])
def search():
     query = request.args.get('query')
     return f'Recherche : {query}'

@app.route('/formulaire' , methods=['GET'])
def formulaire():
     authorfromsearch = request.args.get('author')
     exist = False
     for livre in books:
          if livre['author'] == authorfromsearch:
               exist = True 
               return f'Livre : {livre['title']} ( {livre['year']})'
     if exist == False:
      return "Aucun resultat trouvé"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)