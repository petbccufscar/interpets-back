from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'


class Interpets2019Config(AppConfig):
    name = 'interpets2019'

