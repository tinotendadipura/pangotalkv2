import pdfkit
from  app. models import (InvoiceGenerator)
from django.core.files.base import ContentFile

class MakePDF():
    def subpdf_generator(self,business_ID,order_ID):
        path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf )
        file = pdfkit.from_url(f'http://localhost:9000/account/invoice-generator/{order_ID}', False, configuration=config)
        
        content_file = ContentFile(file, name="pdftringsapme.pdf")
        InvoiceGenerator.objects.create(
                business_ID  =  business_ID,    
                invoice_file =  content_file,     
                order_ID     =  order_ID,        
                
                )
        