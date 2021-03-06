from setuptools import setup, find_packages
setup(
    name='peregrine',
    version="0.1dev",
    description='Peregrine is an opinioned blog system for the Wagtail content management system on the Django Web Framework.',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/FlipperPA/peregrine',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'git+https://github.com/FlipperPA/django-1.11-zappa.git',  # Temporarily monkey patch until Django 2.0 release
        'wagtail>=1.8',
        'wagtailcontentstream',
        'django-bootstrap4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
