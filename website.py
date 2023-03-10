from flask import Flask, url_for, request
from random import choices

app = Flask(__name__)

alertstype = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
planet = {"Меркурий": ["Эта планета ближе всего к Солнцу.", "Он меньше всех остальных планет солнечной системы.",
                        "Его можно колонизировать теми же методами, что и Луну",
                        "Огромные запасы солнечной энергии!", "Огромные залежи ценных руд!"],
           "Венера": ["Венера находится близко к Земле.", "Атмосфера у нее гораздо плотнее земной.",
                      "На ней можно будет жить в воздухе!", "Сила притяжения совпадает с землей.",
                      "На ней много ресурсов!"],
           "Марс": ["Марс близок к Земле.", "На ней много полезный ресурсов.", "Есть вода и атмосфера.",
                    "Также есть небольшое магнитное поле.", "На Марсе есть почва для выращивания растений."],
           "Земля": ["На ней пригодные для жизни условия!", "Есть много воды и можно дышать без скафандра!",
                     "Много животных и растений!", "Красивый и удобный ландшафт!",
                     "Погоди, а зачем мы свою же планету колонизируем?"],
           "Сатурн": ["Планета имеет кольцо из астероидов.", "На нем большое количество газа.",
                      "Сила притяжения почти равная земной.", "У него большое количество спутников.",
                      "Он сам по себе довольно красивый."],
           "Юпитер": ["Он имеет крайне большое количество газа.", "Там может быть новая форма жизни.",
                      "Юпитер выделяет много энергии.", "Имеет небольшие кольца.", "Он крайне огромен!"],
           "Уран": ["Эта планета в безопасности от взрыва Солнца.", "Тут есть ископаемые.", "Много льда и газа!",
                    "Гораздо больше Земли!", "Просто хорошая планета."],
           "Нептун": ["Холодно.", "Далеко.", "Газовый гигант.", "Почти нет солнечной энергии.", "Не стоит."]}


@app.route('/choice/<planet_name>')
def planets(planet_name):
        chosen_alerts = choices(alertstype, k=5)
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
                            <h1>Мое предложение: {planet_name}</h1>
                            <div class="alert alert-{chosen_alerts[0]}" role="alert">
                            {planet[planet_name][0]}
                            </div>
                            <div class="alert alert-{chosen_alerts[1]}" role="alert">
                            {planet[planet_name][1]}
                            </div>
                            <div class="alert alert-{chosen_alerts[2]}" role="alert">
                            {planet[planet_name][2]}
                            </div>
                            <div class="alert alert-{chosen_alerts[3]}" role="alert">
                            {planet[planet_name][3]}
                            </div>
                            <div class="alert alert-{chosen_alerts[4]}" role="alert">
                            {planet[planet_name][4]}
                            </div>
                          </body>'''
                        





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')