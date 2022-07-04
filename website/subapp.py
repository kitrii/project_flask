from flask import Blueprint , render_template

subapp = Blueprint('subapp', __name__)

@subapp.route('/submit', methods = ["GET","POST"])
def submit():
    return render_template('subapp.html')
    
