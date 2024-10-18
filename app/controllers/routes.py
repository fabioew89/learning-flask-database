from flask import request, render_template, redirect, url_for 
from app import app
from app.models import User, db

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

########## ########## ########## ########## ########## 
# Rota 1
@app.route('/users')
def user_list():
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    return render_template('user/list.html', users=users)









# Rota 2
@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")

# Rota 3
@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)

# Rota 4
@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user/delete.html", user=user)