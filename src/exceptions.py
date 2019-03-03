from . import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    return render_template('./exceptions/404_notfound.html', error=error), 404


@app.errorhandler(400)
def bad_request(error):
    return render_template('./exceptions/400_badrequest.html', error=error), 400
