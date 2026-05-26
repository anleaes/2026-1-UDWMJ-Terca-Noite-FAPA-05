LOGIN_URL = '/accounts/user_login/'
EMPLOYEE_LOGIN_URL = '/accounts/employee_login/'


def user_is_employee(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return hasattr(user, 'employee_profile')


def user_is_client(user):
    if not user.is_authenticated:
        return False
    return hasattr(user, 'client_profile')


def get_client_login_redirect_url():
    return '/'


def get_employee_login_redirect_url():
    return '/cinema/'
