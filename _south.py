__author__ = 'jb'

def try_initialize_south():
    try:
        import south
    except ImportError:
        # No south in pypath
        return
    from south.modelsinspector import add_introspection_rules

    from fields import DictionaryField
    rules = [(
         (DictionaryField,),
         [],
         {
             'type': ['type', {}],
             },
         )]
    add_introspection_rules(rules, ["^django_dict\.fields\.DictionaryField"])

try_initialize_south()

