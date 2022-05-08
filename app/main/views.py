from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import Comment,User
from .forms import CommentForm,UpdateProfile
from .. import db,photos

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

@main.route('/categories/humour/comment/new/<id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(pitch_id=pitch.id,pitch_title=title,pitch_comment=comment,user=current_user)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.humour',id = pitch.id ))

    title = f'{pitch.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.profile',uname=uname))
