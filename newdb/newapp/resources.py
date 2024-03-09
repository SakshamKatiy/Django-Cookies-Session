from import_export import resources
from .models import students


class studentResources(resources.ModelResource):
    class Meta:
        model = students