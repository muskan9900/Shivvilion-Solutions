from django.core.management.base import BaseCommand
import uvicorn

# creating managment helper commands 

class Command(BaseCommand):
    help="Run the Django Application with Uvicorn"
    def handle(self, *args, **options):
    #    we will return uvicorn run() over here
        uvicorn.run("ASGI_EXAMPLE.asgi:application", host="127.0.0.1",port=8000,reload=True)

