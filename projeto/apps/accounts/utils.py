LOGIN_URL = '/accounts/user_login/'


def user_is_employee(user):
    if not user.is_authenticated:
        return False
    return user.is_superuser or user.is_staff


def user_is_client(user):
    if not user.is_authenticated:
        return False
    return hasattr(user, 'client_profile')
