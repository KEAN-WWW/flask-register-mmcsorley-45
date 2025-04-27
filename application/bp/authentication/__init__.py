from flask import Blueprint, render_template, redirect, url_for, flash

from application.database import User, db
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')
@authentication.route('/dashboard')
def dashboard():
    # user_records = User.all()

    return render_template('dashboard.html')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    def registration():
        form = RegisterForm()

        if form.validate_on_submit():
            # Create a new user with form data
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data  # You should hash the password in production!
            )

            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful!', 'success')
            return redirect(url_for('authentication.dashboard'))

        return render_template('registration.html', form=form)


