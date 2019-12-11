from app import app, db
from app.models import Post, Block, Contact
import datetime

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Block': Block, 'Post': Post, 'Contact': Contact}

@app.template_filter('prettytime')
def prettytime(s):
    return s.strftime('%b %d, %Y')

# app packages
# from flask import Flask, render_template, jsonify, request, Response, redirect, url_for, flash
# import time
# import os
# import json
# from flask_mail import Mail, Message
# from functools import wraps

# # instantiates web server app
# app = Flask(__name__)

# ''' What I Need:
# - top section
# - about me
# - portfolio 
# - contact form ''' 

# # ------------- Mail Server Configuration ----------------------
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# app.config.update(dict(
# 	DEBUG=True,
# 	#EMAIL SETTINGS
# 	MAIL_SERVER='smtp.gmail.com',
# 	MAIL_PORT=587,
# 	MAIL_USE_SSL=False,
#     MAIL_USE_TLS=True,
# 	MAIL_USERNAME = 'ben10devera@gmail.com',
# 	MAIL_PASSWORD = 'G*ucla10!'
# ))


# mail = Mail(app)
# # ---------------------------------------------------------------

# # -------------------------------- Website Functionality Routes -------------------------------------
# @app.route('/')
# def index():
#     return render_template('index.html')
# #------------------------------------------------------------------------------

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', debug=True, port=port)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html')

# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)