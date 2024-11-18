from app.models import Client, Domain

tenant = Client(schema_name = "seedco",name = "SeedCo Company")
tenant.save()

domain = Domain(domain = "seedco.localhost", tenant = tenant, is_primary = True)
tenant.save()
