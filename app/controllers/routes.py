from flask import request, render_template, flash, redirect, url_for
from app import app, db
from app.models.model import Users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        #print variaveis username e email
        print(f'username {username}, email: {email}')

        if username and email:
            new_user = Users(username=username, email=email)

            try:
                db.session.add(new_user)
                db.session.commit()
                flash(f'Usuario adicionado com sucesso', 'success')
                return redirect(url_for('index'))

            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao adicionar usuario {e}', 'error')
                return redirect(url_for('add_user'))
        else:
            flash(f'preencha os campos', 'error')
            return redirect('add_user')
    
    return render_template('add_user.html')
