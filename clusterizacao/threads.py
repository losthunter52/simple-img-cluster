from django_thread import Thread
from .models import *

class SimpleConsumer(Thread):

    def __init__(self, object):
        Thread.__init__(self)
        self.object = object

    def run(self):
        x = 1

