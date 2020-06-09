# -*- coding: utf-8 -*-
"""

"""

from flask import render_template, Blueprint


error_pages = Blueprint("error_handlers", __name__)


@error_pages.errorhandler(404)
def error_404_page_not_found(error):
    """
    An error handler for when 404 error happens.

    :param error:
    :return:
    """
    return render_template('404.html'), 404


@error_pages.errorhandler(500)
def error_500_server_error(error):
    """
    An error handler for when 404 error happens.

    :param error:
    :return:
    """
    return render_template('500.html'), 500
