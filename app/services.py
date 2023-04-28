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
    if not has_been_created_today() :
        generator = pipeline(task='text-generation', model='gpt2')
        content_list = generator("The software engineering")
        for content in content_list:
            post_to_db(content["generated_text"])
        return content
    
    return []

def post_to_db(text):
    try:
        p = Post(content=text.rsplit('.', 1)[0] + ".", created_date=datetime.now())
        db.session.add(p)
        db.session.commit()
        return "Success"
    except Exception as e:
        return str(e)

def has_been_created_today():
    return Post.query.filter_by(created_date=datetime.today()).first()

def delete_post(id):
    try:
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return "Success"
    except Exception as e:
        return str(e)
