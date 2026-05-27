from django.db.models import Q


def orders_for_user(user):
    """Orders owned by this login (direct user FK or linked client profile)."""
    if not user.is_authenticated:
        return Q(pk__in=[])
    filters = Q(user=user)
    if hasattr(user, 'client_profile'):
        filters |= Q(client=user.client_profile)
    return filters


def user_owns_order(user, order):
    if not user.is_authenticated:
        return False
    if order.user_id == user.id:
        return True
    if order.client_id and hasattr(user, 'client_profile'):
        return order.client_id == user.client_profile.id
    return False


def tickets_for_user(user):
    if not user.is_authenticated:
        return Q(pk__in=[])
    filters = Q(order__user=user)
    if hasattr(user, 'client_profile'):
        filters |= Q(order__client=user.client_profile)
    return filters
