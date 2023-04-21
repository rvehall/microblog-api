from app import app, db
from app.models import Post
import app.services as service

@app.route('/posts', methods=['GET'])
def get_posts():
    return service.get_posts()

@app.route('/posts', methods=['Post'])
def post_post():
    return service.generate_posts()