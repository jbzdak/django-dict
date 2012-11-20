__author__ = 'jb'


from django.db.models import ForeignKey

class DictionaryField(ForeignKey):
    def __init__(self, type, **kwargs):
        self.type = type
        kwargs['related_name'] = "+"
        if "to" not in kwargs:
            kwargs['to'] = "django_dict.dictionary"
        if "limit_choices_to" not in kwargs:
            kwargs['limit_choices_to'] = {
                "type" : type,
                "active" : True
            }
        super(DictionaryField, self).__init__(**kwargs)

