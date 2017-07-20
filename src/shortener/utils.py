import random
import string
from django.conf import settings
SHORTCODE_MIN=getattr(settings,"SHORTCODE_MIN",6)
def code_generator(size=SHORTCODE_MIN,char=string.ascii_lowercase + string.digits):
    #new_code=''
    #for _ in range(size):
    #    new_code+=random.choice(char)
    #return new_code
    return ''.join(random.choice(char) for _ in range(size))
def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code=code_generator()
    rlass=instance.__class__
    qs_exits=rlass.objects.filter(shortcode=new_code).exists()
    if qs_exits:
        return create_shortcode(size=size)
    return new_code
