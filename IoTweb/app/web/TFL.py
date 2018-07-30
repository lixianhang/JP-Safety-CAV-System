from app.web import web
from flask import request, jsonify
from app.forms.tfl_search import SearchForm
from app.spyder.search_tfl import search_on_tfl
@web.route('/tfl/search')
def search():
    form=SearchForm(request.args)
    query=form.data
    result=search_on_tfl.search_by_query (query)
    return jsonify(result)