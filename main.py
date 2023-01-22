from flask import Flask

from movie.views import movie_bp

from rating.views import rating_bp

app = Flask(__name__)

app.register_blueprint(movie_bp, url_prefix='/movie')
app.register_blueprint(rating_bp, url_prefix='/rating')


@app.route('/')
def index():
    return '<h1>Main page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
