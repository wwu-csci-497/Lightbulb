from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from bettercrative import db
from bettercrative.models import Classroom
from bettercrative.classrooms.forms import ClassroomForm

classrooms = Blueprint('classrooms', __name__)


@classrooms.route("/classroom/new", methods=['GET', 'POST'])
@login_required
def new_classroom():
    form = ClassroomForm()
    if form.validate_on_submit():
        classroom = Classroom(classroom_Name=form.classroom_Name.data, key=form.key.data, author=current_user)
        db.session.add(classroom)
        db.session.commit()
        flash('New Classroom Created!', 'success')
    return render_template('create_classroom.html', title='New Classroom', form=form)
