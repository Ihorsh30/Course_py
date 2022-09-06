from django.http import Http404


class StaffPermissionMixin:

    def has_permission(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404("Sorry you can't make changes to products as you are not a staff but you become one")
        return super().dispatch(request, *args, **kwargs)



