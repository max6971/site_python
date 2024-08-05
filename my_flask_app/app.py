from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

# Страница блога
@app.route('/blog')
def blog():
    comments = [
        {"author": "Мэтт Мердок", "text": "Все хорошо, я на Гаваях", "photo": "../static/kard1.png"},
        {"author": "Дженнифер Лоуренс", "text": "Приветю Как долетел?", "photo": "../static/kard3.png"}
    ]
    return render_template('blog.html', comments=comments)

# Страница контактов
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Обработка формы
        name = request.form['name']
        comment = request.form['comment']
        # В реальном приложении здесь будет сохранение комментария в базу данных
        return redirect(url_for('contacts'))
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)