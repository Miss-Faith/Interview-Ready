from flask import render_template,request
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():
  '''
    View root page function that returns the index page and its data
  '''

  return render_template('index.html')

@main.route('/categories/')
def categories():

    '''
    View categories page function that returns the pitch details page
    '''

    return render_template('categories.html')

@main.route('/categories/humour')
def humour():

    '''
    View humour pitch page function that returns the various pitch in humour category
    '''
    
    return render_template('humour.html')

@main.route('/categories/humour/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):