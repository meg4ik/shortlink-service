import random
import string

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
