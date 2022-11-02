import random
import string
from browser_app.models import User
from secrets import token_hex

def create_shortlink():
    characters = string.ascii_letters + string.digits + "-"
    return ''.join(random.choice(characters) for _ in range(6))

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_fake_user():
    try:
        fakeuser = User.objects.get(username='fakeuser')
    except:
        User.objects.create_user('fakeuser', token_hex(16))
    return User.objects.get(username='fakeuser')