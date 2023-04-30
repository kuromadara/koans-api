from django.contrib import admin

"""
    Register all models automatically
        try except block is used to avoid error when a model is already registered before
"""

from django.apps import apps


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
print(models)
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
