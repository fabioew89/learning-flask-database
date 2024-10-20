from flask import render_template, request, flash, redirect
from app import app, db
from app.models.model import Users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')

    print(f'username {username}, email: {email}')

    if username and email:
        new_user = Users(username=username, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f'Usuario adicionado com sucesso', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar usuario {e}', 'error')
        
        return redirect('/')
    else:
        flash(f'preencha os campos', 'error')
        return redirect('/')