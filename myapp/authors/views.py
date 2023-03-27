from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

author = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')

AUTHORS = {
    1: 'Bob',
    2: 'John',
    3: 'Mike'
}

ARTICLES = {
    1: {
        'text': 'my favorite article',
        'author': 1
    },
    2: {
        'text': 'Статья про  python',
        'author': 3
    },
    3: {
        'text': 'Статья про  Flask',
        'author': 2
    },
    4: {
        'text': 'Статья про  Django',
        'author': 1
    }
}


@author.route('/')
def author_list():
    return render_template(
        'authors/list.html',
        authors=AUTHORS,
        articles=ARTICLES
    )


@author.route('/<int:pk>')
def get_article(pk: int):
    try:
        name=ARTICLES[pk]['author']
    except KeyError:
        raise NotFound(f'Article {pk} not found')    
    return render_template(
        'authors/detail.html',       
        article=ARTICLES[pk],
        author=AUTHORS[name]

    )

