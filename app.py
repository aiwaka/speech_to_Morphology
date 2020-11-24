from flask import Flask, render_template, request
from janome.tokenizer import Tokenizer

app = Flask(__name__)

t = Tokenizer(wakati=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def exec():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        outputs = t.tokenize(rawtext)
        output = [str(el) for el in outputs]
    else:
        output = ["null"]
    return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
