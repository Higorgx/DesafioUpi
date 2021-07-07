from settings import *
import json


# Initializing our database
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    author = db.Column(db.String(80), nullable=False)
    read = db.Column(db.Boolean(80), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'author': self.author, 'read': self.read}
            # this method we are defining will convert our output to json

    def delete_book(_id):
        Book.query.filter_by(id=_id).delete()
        db.session.commit()

    def add_book(_title, _author, _read):
        # creating an instance of our Movie constructor
        new_book = Book(title=_title, author=_author, read=_read)
        db.session.add(new_book)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_Book():
        return [Book.json(book) for book in Book.query.all()]
    
    def get_book(_id):
        return [Book.json(Book.query.filter_by(id=_id).first())]

    def update_book(_id, _title, _author, _read):
        book_to_update = Book.query.filter_by(id=_id).first()
        book_to_update.title = _title
        book_to_update.author = _author
        book_to_update.read = _read
        db.session.commit()
        