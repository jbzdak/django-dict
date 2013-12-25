
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
#             'render_pattern': ['render_pattern', {'default', None}],
             },
         )]
    add_introspection_rules(rules, ["^django_dict\.fields\.DictionaryField"])

try_initialize_south()

