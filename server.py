import os
import random

from bottle import route, run
import sayings

a = []

def generate_message():
    x = "{} {} {} {} {}".format(random.choice(sayings.beginnings), random.choice(sayings.subjects), random.choice(sayings.verbs), random.choice(sayings.actions), random.choice(sayings.ends))
    x = str(x)
    message_dict= {'message': x}
    return str(message_dict)
def many_message(n):
    for i  in range(1, n + 1):
      x = "{} {} {} {} {}".format(random.choice(sayings.beginnings), random.choice(sayings.subjects), random.choice(sayings.verbs), random.choice(sayings.actions), random.choice(sayings.ends))
      x = str(x)
      a.append(x)
    messages_dict = {'messages':a}
    return messages_dict


@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html


@route("/api/generate/")
def first():
   return generate_message()

@route("/api/generate/<n:int>")
def second(n):
  return many_message(n)

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)


