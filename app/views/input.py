from pyramid.view import view_config

@view_config(route_name='input', renderer='../templates/input.jinja2')
def my_view(request):
    return {}
