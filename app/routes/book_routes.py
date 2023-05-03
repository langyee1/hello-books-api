from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("",methods=["GET"])
def handle_books():
    books = Book.query.all()
    books_list = []

    for book in books:
        books_list.append(book.make_book_dictionary())

    return jsonify(books_list),200


@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("/<id>",methods=["GET"])
def handle_book(id):
    book = validate_book(id)
    
    return jsonify(book.make_book_dictionary()),200

@books_bp.route("/<id>", methods=["PUT"])
def update_cat(id):
    book = validate_book(id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"book {book.title} successfully updated", 200)


# DELETE ONE ENDPOINT
@books_bp.route("/<id>", methods=["DELETE"])
def delete_cat(id):
    book = validate_book(id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"book {book.title} successfully deleted", 200)


def validate_book(id):
    try:
        id = int(id)
    except: 
        abort(make_response({"message": f"{id} was invalid"},400))

    book = Book.query.get(id)

    if not book: 
        abort(make_response({"message": f"{id} was not found"},404))

    return book