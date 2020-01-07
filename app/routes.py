from app import APP, db
from flask import render_template, redirect, request, url_for, send_from_directory
from app.models import Post, Contact
from sqlalchemy import desc 

@APP.route('/')
def index():
    posts = Post.query.order_by(desc(Post.date)).all()[:3]
    return render_template('index.html', posts=posts)

@APP.route('/blog')
def blog():
    posts = Post.query.order_by(desc(Post.date)).all()
    return render_template('blog.html', posts=posts)

@APP.route('/blog/<id>')
def blog_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return redirect(url_for('index'))
    return render_template('blog_post.html', post=post)

@APP.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@APP.route('/contact', methods=["POST"])
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

@APP.route('/robots.txt')
@APP.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@APP.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

