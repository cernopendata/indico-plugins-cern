from setuptools import setup


setup(
    name='indico_foundationsync',
    version='1.0.4',
    url='https://gitlab.cern.ch/indico/indico-plugins-cern',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    py_modules=('indico_foundationsync',),
    zip_safe=False,
    install_requires=[
        'indico>=1.9.10',
        'cx_Oracle',
    ],
    entry_points={'indico.plugins': {'foundationsync = indico_foundationsync:FoundationSyncPlugin'}}
)
