#from flask import Blueprint, jsonify, make_response,abort

"""hello_world_bp = Blueprint("hello_world", __name__)


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON",methods=["GET"])
def say_hello_json():
    return{
        "name":"ADA",
        "message":"hi",
        "Hobbies":["netflix","chess"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body
    """

#book hard-coding starts now...

#books_bp = Blueprint("books", __name__, url_prefix="/books")

"""
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def make_book_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] """

"""
@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append(book.make_book_dict())
    return jsonify(books_response)

@books_bp.route("/garcia-marquez",methods=["POST"])
def register_book():
    new_book = Book(7,"100 años de soledad","una historia de realismo magico")
    books.append(new_book)
    result = handle_books()
    return result

@books_bp.route("/<book_id>",methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)
    return book.make_book_dict()
        
def validate_book(book_id):
    try:
        book_id = int(book_id)

    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))

    for book in books: 
        if book.id == book_id:
            return book
    
    abort(make_response({"message": f"book {book_id} not found"}, 404))

"""        
#connecting FLAKS app to database to be able to not only read, but to create, update, delete... all of CRUD


