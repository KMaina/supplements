import datetime

from app.main import db
from app.main.model.blog import Blog


def create_new_blog(data):
    try:
        new_blog = Blog(
            title=data['title'],
            body=data['body'],
            published_on=datetime.datetime.utcnow()
        )
        save_changes(new_blog)
        response_object = {
            'status': 'success',
            'message': 'Blog successfully created'
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_blogs():
    return Blog.query.all()

def get_a_blog(id):
    return Blog.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
