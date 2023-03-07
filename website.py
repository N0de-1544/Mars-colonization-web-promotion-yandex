from flask import Flask, url_for,request


app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name"  placeholder="Введите Имя" name="name">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите Фамилию" name="surname">
                                    <input type="email" class="form-control" id="email" placeholder="Введите e-mail" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое ваше образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Дошкольное образование</option>
                                          <option>Начальное общее образование</option>
                                          <option>Основное общее образование</option>
                                          <option>Среднее общее образование</option>
                                          <option>Среднее профессиональное образование</option>
                                          <option>Бакалавриат</option>
                                          <option>Магистратура</option>
                                          <option>Специалитет</option>
                                        </select>
                                    </div>
                                    <div class="form-group form-check>
                                        <label for="form-check">Какие у Вас есть профессии?</label><br>
                                        <input type="checkbox" name="prof_1" value="engi-res"> Инженер-исследователь<br>
                                        <input type="checkbox" name="prof_2" value="pilot"> Пилот<br>
                                        <input type="checkbox" name="prof_3" value="builder"> Строитель<br>
                                        <input type="checkbox" name="prof_4" value="exobio"> Экзобиолог<br>
                                        <input type="checkbox" name="prof_5" value="radprot"> Специалист по радиационной защите<br>
                                        <input type="checkbox" name="prof_6" value="doctor"> Врач<br>
                                        <input type="checkbox" name="prof_7" value="cyberengi"> Киберинженер<br>
                                        <br>       
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов работать за идею.</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')