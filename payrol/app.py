from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('jinja.html')

@app.route('/jinjatest')
def jinjatest():
    message = 'The <strong>sum</strong> of the numbers is: '
    items = ['widget', 'doodad', 'thingie', 'whatsit']
    return render_template('jinjatest.html', message=message, items=items)


#Custom Error Handler to avoid some code exception messages on HTML output
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

