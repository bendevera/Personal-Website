from app import app 
from flask import render_template, redirect
from app.models import Post

@app.route('/')
def index():
    posts = Post.query.all()[:3]
    return render_template('index.html', posts=posts)

@app.route('/blog')
def blog():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<id>')
def blog_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return redirect('index')
    return render_template('blog_post.html', post=post)