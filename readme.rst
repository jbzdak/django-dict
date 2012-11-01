

Django dictionaries
===================

Provides dictionary model that allows one to associate other models with arbitrary dictionary items (or tags). Since
there will be many kinds of dictionaries dictionary entries have `type` property that facilitate this.

Concept of activity
-------------------

Dictionary entities can also active or inactive, where being inactive means that no new model instances might be associated to
inactive dictionary entry.

When editing models (for example in admin app) logic is as follows: one can associate model instance with a dictionary
entry iff: dictionary entry has a proper type, is active or was previously associated with this model (even if inactive).

We also provide model form subclass that implements this edit logic.


Dictionary types are stored in `settings.DICTIONARY_CHOICES` which is a normal django choice touple.

Dictionaty items have three properties:

type:
    String denoting type of the dictionary item.
name:
    Name of the dictionary item.
active:
   if dictionaty entry is active or not.


What is provided apart from model class:

* Admin view
* Field that allows easier association of models with dictionary instances.

Examples
========

In settings.py::

 DICTIONARY_CHOICES = (
     ("status", "Status"),
     ("tag", "Tag")
 )

In models::

  from django_dict import fields
  class FooBar(models.Model):
        tag = fields.DictionaryField(type="status")

In forms::

 from django_dict import forms
 class FooForm(forms.DictionayModelForm):
    class Meta:
        model = FooBar
