from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'test_app'}