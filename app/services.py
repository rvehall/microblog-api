from app.models import Post
from app import db
from datetime import datetime
from transformers import pipeline


def get_posts():
    posts = list(Post.query.all())
    data = []
    for p in posts:
        data.append(Post.as_dict(p))

    return data

def generate_posts():
    if check_if_created():
        generator = pipeline(task='text-generation', model='gpt2')
        content = generator("The software engineering industry is rapidly evolving.", num_return_sequences=5, return_full_text=True)

        for text in content:
            post_to_db(text)

        return content
    
    return []

def post_to_db(post):
    try:
        p = Post(content=post["generated_text"], created_date=datetime.now())
        db.session.add(p)
        db.session.commit()
        return "Success"
    except Exception as e:
        return str(e)

def check_if_created():
    post = Post.query.filter_by(created_date=datetime.today()).first()

    return post