"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""


import MySQLdb
from app import app, chat
from flask import jsonify, render_template, request, redirect, url_for, flash
from app.forms import RegisterForm
# from app.forms import LoginForm

from app import mysql

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route("/register/", methods=["POST"])
def register():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        #cur = MySQLdb.connect("localhost", "root", "", "capstone")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_profiles(full_name, username, email, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))
        mysql.connection.commit()
        cur.close()

        redirect(url_for('chat_compbot'))

    return redirect(url_for('home'))


@app.route('/chat/compbot', methods=["GET","POST"])
def chat_compbot():
    """Render the website's chat page for compbot"""
    if request.method == 'POST':
        userinput = request.form['userinput']
        response = chat.chatbot_response()
        return jsonify({"response": response })
    return render_template('compbot.html')

@app.route('/chat/admin')
def chat_admin():
    """Render the website's chat page for admin"""
    return render_template('admin.html')

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'danger')
#     return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
# @login_manager.user_loader
# def load_user(id):
#     return UserProfile.query.get(int(id))


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
