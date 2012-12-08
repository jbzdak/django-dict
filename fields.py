

__author__ = 'jb'

from django.db.models import ForeignKey
from django.forms.models import ModelChoiceField

class PatternedModelChoiceField(ModelChoiceField):

    pattern = None

    def label_from_instance(self, obj):
        return self.pattern.format(field = obj)

class DictionaryField(ForeignKey):
    def __init__(self, type, render_pattern = None, **kwargs):
        """

        :param type: Type of DjangoDict this field is bound to
        :param render_pattern: Pattern (as used by `str.format`)
            that will render contents of this field. If None will use
            :meth:`Dictionary.__unicode__`, if `__label__` will render only
            item label. Defaults to None
        :param kwargs: Accepts also all arguments of ForeignKey.
        """
        self.type = type
        self.render_pattern = render_pattern
        kwargs['related_name'] = "+"
        if "to" not in kwargs:
            kwargs['to'] = "django_dict.dictionary"
        if "limit_choices_to" not in kwargs:
            kwargs['limit_choices_to'] = {
                "type" : type,
                "active" : True
            }

        super(DictionaryField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {

        }
        if self.render_pattern is not None:
            if self.render_pattern == "__label__":
                class FormField(PatternedModelChoiceField):
                    pattern = u"{field.label}"
            else:
                class FormField(PatternedModelChoiceField):
                    pattern = self.render_pattern

            defaults['form_class'] = FormField

            defaults.update(kwargs)

        return super(DictionaryField, self).formfield(**defaults)



