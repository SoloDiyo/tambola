from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')
lis = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        textbox_value = request.form['textbox_name']
        lis.append(int(textbox_value))
        lis.sort()
            # Process the textbox value here (e.g., print it, store it in a database)
        return render_template('main2.html', value=lis)
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
