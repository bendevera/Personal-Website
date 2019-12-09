from sqlalchemy import Integer, ForeignKey, String, Column, Float
from datetime import datetime
from app import db  

'''
Flask Migration Process:
1. (just initially) flask db init (initializes db)
2. (after each change) flask db migrate -m "message" (creates migration)
3. flask db upgrade (performs migration) 
'''

class Post(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    date = Column(db.DateTime, default=datetime.utcnow)
    abstract = Column(String, nullable=True)
    blocks = db.relationship('Block', backref="post")


class Block(db.Model):
    __tablename__ = "blocks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    data = Column(String)
    attribute = Column(String, nullable=True)
    order = Column(Integer)
    post_id = Column(Integer, ForeignKey('posts.id'))

'''
Block Types:

1. text

data - text of the block
attribute - color for styling 

2. image

data - path for image file (url or local file path)
attribute - css for specific styling

3. code

data - text to be styled like code
attribuet - ignored
'''