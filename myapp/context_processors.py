

def day_night_mode(request):
    mode = request.session.get('mode', 'day')
    return {'mode': mode}