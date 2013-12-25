from distutils.core import setup
import os


def load_package_data(package, root_dir):

    def iter():
        folder  = os.path.join(package, root_dir)
        for root, dirs, files in os.walk(folder):
            folder = os.path.sep.join(root.split(os.path.sep)[1:])
            for file in files:
                yield os.path.join(folder, file)

    return list(iter())


package_data = load_package_data('django_dict', 'locale')


setup(
    name='django-dict',
    version='1.0',
    packages=['django_dict'],
    package_data = {
        "django_dict" : package_data
    },
    url='foo',
    license='BSD-style two clause',
    author='Jacek Bzdak',
    author_email='jbzdak@gmail.com',
    description='Reusable app that adds simple tagging',
    classifiers="""
Development Status :: 5 - Production/Stable
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: Polish
Natural Language :: English
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
    """
)
