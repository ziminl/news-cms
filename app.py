from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define a list to store news articles
articles = []


@app.route('/')
def index():
    return render_template('index.html', articles=articles)


@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Create a new article and add it to the list
        article = {'title': title, 'content': content}
        articles.append(article)
        return redirect('/')
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)