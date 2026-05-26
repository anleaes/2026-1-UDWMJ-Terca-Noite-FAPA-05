from .utils import user_is_client, user_is_employee


def auth_flags(request):
    return {
        'user_is_employee': user_is_employee(request.user),
        'user_is_client': user_is_client(request.user),
    }
