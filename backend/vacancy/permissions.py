from dashboard.permissions import BaseIsOwnerOrReadOnly


class IsOwnerOrReadOnly(BaseIsOwnerOrReadOnly):
    owner_field = 'owner'
    link_to_owner_field = 'company'
