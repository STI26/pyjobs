from dashboard.permissions import BaseIsOwnerOrReadOnly


class IsOwnerOrReadOnly(BaseIsOwnerOrReadOnly):
    owner_field = 'profile'
    link_to_owner_field = 'owner'
