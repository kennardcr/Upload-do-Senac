from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Olá! Este é meu primeiro sistema web."

if __name__ == "__main__":
    app.run(debug=True)