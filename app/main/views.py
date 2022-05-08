from flask import render_template
from . import main

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
    View categories page function that returns the pitch details page and its data
    '''

    return render_template('categories.html')