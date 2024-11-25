from celery import shared_task
from app.models import Client, Domain


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"




@shared_task(bind=True)
def create_comapany_subdomain_task(temp_company_domain,  final_domain,task_id):
    try:
        # excute this part once the page have loaded
        
        tenant         = Client(schema_name = temp_company_domain,name = temp_company_domain )
        tenant.save()
                
        
        domain_info    = Domain(domain = final_domain, tenant = tenant, is_primary = True)
        domain_info.save()

        return "Done"

    
    
    
    except Exception as e:
        # Handle any other unforeseen exceptions
        print(f"An error occurred: {str(e)}")
        return "Done"

    