from app import app
import app.services as service


@app.route('/', methods=['GET'])
def default():
    return "Hello, world!"

@app.route('/posts', methods=['GET'])
def get_posts():
    return service.get_posts()

@app.route('/posts', methods=['Post'])
def post_post():
    return service.generate_posts()