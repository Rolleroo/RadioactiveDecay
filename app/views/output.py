from pyramid.view import view_config

@view_config(route_name='output', renderer='../templates/output.jinja2')
def my_view(request):
    # this is the value the user entered on the input page
    user_choice = request.params.get('userChoice')
    # call a function that performs the calculation
    results = [
        {
            'a': 'banana ' + user_choice,
            'b': 'apple ' + user_choice,
        },
        {
            'a': 'chicken ' + user_choice,
            'b': 'chips ' + user_choice,
        },
    ]
    return {'results': results}
