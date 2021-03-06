from pyramid.view import view_config
from pyramid.httpexceptions import HTTPCreated, HTTPBadRequest
from pyramid.response import Response
import logging

_LOG = logging.getLogger(__name__)
def _raise_HTTP_from_msg(msg):
    raise HTTPBadRequest(body=_err_body(msg))

def _extract_dot_from_http_call(request, **kwargs):
    """Returns the dot blob from `kwargs` or the request.body"""
    try:
        if 'dot' in kwargs:
            dot = repr(kwargs.get('dot', {}))
        else:
            dot = request.body

        dot = dot.strip()
        assert dot
    except:
        _LOG.exception('Exception dot content in _extract_dot_from_http_call')
        _raise_HTTP_from_msg('"dot" content must be passed in.')
    return dot

def _extract_and_validate_dot(request, kwargs):
    dot = _extract_dot_from_http_call(request, **kwargs)
    #TODO validation here...
    return dot

@view_config(route_name='post_dot', renderer='templates/mytemplate.pt', request_method='POST')
def post_dot(request):
    "Open Tree API methods relating to creating (and importing) resources"
    try:
        lines = [i.strip() for i in request.POST['dot'].file.readlines()]
    except:
        err = 'dot file must be passed in as a "dot" argument'
        raise HTTPBadRequest(err)
    dot = " \\n".join(lines)
    err = ''
    if "'" in dot:
        err = "Sorry. I found a single-quote in your dot file, and that breaks our rendering code"
        raise HTTPBadRequest(err)
    return {'dot': dot, 'error': err}


@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
    return {}
