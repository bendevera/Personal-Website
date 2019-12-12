from app import app, db
from flask import render_template, redirect, request, url_for
from app.models import Post, Contact
from sqlalchemy import desc 

@app.route('/')
def index():
    posts = Post.query.order_by(desc(Post.date)).all()[:3]
    return render_template('index.html', posts=posts)

@app.route('/blog')
def blog():
    posts = Post.query.order_by(desc(Post.date)).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<id>')
def blog_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return redirect(url_for('index'))
    return render_template('blog_post.html', post=post)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=["POST"])
def contact():
    content = request.form 
    print(content)
    try:
        new_contact = Contact(email=content['email'], message=content['message'])
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        print(e)
    return redirect(url_for('index'))
