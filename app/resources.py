from import_export import resources
from app.models import CountryCodes
 
class CountryCodesResource(resources.ModelResource):
    class Meta:
        model = CountryCodes