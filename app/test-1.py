from app.models import Client, Domain

tenant = Client(schema_name = "public",name = "Public")
tenant.save()

domain = Domain(domain = "localtest.me", tenant = tenant, is_primary = True)
tenant.save()
Domain.objects.create(domain = "localtest.me", tenant = tenant, is_primary = True)

tenant = Client.objects.filter(schema_name = "public").first()