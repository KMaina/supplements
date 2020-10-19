from flask import request
from flask_restx import Resource

from ..util.dto import BlogDto
from ..service.blog_service import create_new_blog, get_a_blog, get_all_blogs, delete_blog

api = BlogDto.api
_blog = BlogDto.blog


@api.route('/')
class BlogList(Resource):
    @api.doc('list_of_blogs')
    @api.marshal_list_with(_blog, envelope='data')
    def get(self):
        """List of all blogs"""
        return get_all_blogs()

    @api.response(201, 'Blog successfully created.')
    @api.doc('create a new blog')
    @api.expect(_blog, validated=True)
    def post(self):
        """Create a new Blog"""
        data = request.json
        return create_new_blog(data=data)

@api.route('/<id>')
@api.param('id', 'The Blog identifier')
@api.response(404, 'Blog not found.')
class Blog(Resource):
    @api.doc('get a blog')
    @api.marshal_with(_blog)
    def get(self, id):
        """get a blog given its identifier"""
        blog = get_a_blog(id)
        if not blog:
            api.abort(404)
        else:
            return blog

    @api.doc('delete a blog')
    # @api.marshal_with(_blog)
    def delete(self, id):
        """get a blog given its identifier"""
        blog = delete_blog(id)
        return blog
