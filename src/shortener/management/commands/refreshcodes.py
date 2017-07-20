from django.core.management.base import BaseCommand,CommandError
from shortener.models import RakibbUrl

class Command(BaseCommand):
    help ='refresh all exitsing short code'
    def add_arguments(self,parser):
        parser.add_argument('--items',type=int)
    def handle(self,*args,**options):

        return RakibbUrl.objects.refresh_shortcode(items=options['items'])
