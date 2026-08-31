from flask import Flask, request, render_template_string
from count_utils import count_vowels

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="pt-br">
<head><meta charset="utf-8"><title>Vowels Counter</title></head>
<body>
  <h1>Vowel Counter</h1>
  <form method="get" action="/">
    <input id="texto" name="texto" value="{{ texto }}">
    <button id="contar" type="submit">Contar</button>
  </form>
  <p>Vowels: <span id="result">{{ result }}</span></p>
</body>
</html>
"""

@app.route("/")
def index():
    texto = request.args.get("texto", "")
    result = "" if texto == "" else count_vowels(texto)
    return render_template_string(PAGE, texto=texto, result=result)

if __name__ == "__main__":
    app.run(port=5000)