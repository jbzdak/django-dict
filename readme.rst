

Django dictionaries
===================

Provides dictionary model that allows one to associate other models with
arbitrary tags. Also you can define different types of these tags,
for example a tag for status of something, and other for each department of
your company.

Each ``Dictionaty`` entity has an associated type.

Features
--------

Dictionary entities can also active or inactive, where being inactive means
that no new model instances might be associated to
inactive dictionary entry, but ones that were associated earlier stay
unchanged.


When editing models (for example in admin app) logic is as follows: one can
associate model instance with a dictionary
entry iff: dictionary entry has a proper type, is active or was previously
associated with this instance.

We also provide model form subclass that implements this edit logic.

Dictionary types are stored in ``settings.DICTIONARY_CHOICES`` which is a normal django choice touple.

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

In ``settings.py``:

.. code-block:: python

    DICTIONARY_CHOICES = (
     ("status", "Status"),
     ("tag", "Tag")
    )

In models:

.. code-block:: python

  from django_dict import fields
  class FooBar(models.Model):
        tag = fields.DictionaryField(type="status")

In forms:

.. code-block:: python

 from django_dict import forms
 class FooForm(forms.DictionayModelForm):
    class Meta:
        model = FooBar
