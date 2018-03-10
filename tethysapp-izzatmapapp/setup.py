import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'izzatmapapp'
release_package = 'tethysapp-' + app_package
app_class = 'izzatmapapp.app:Izzatmapapp'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='&quot;Geospatial&quot;,&quot;ArcGIS&quot;',
    description='This is the coolest Map App EVER',
    long_description='',
    keywords='',
    author='Izzat Habib Mukattash',
    author_email='izzatmukattash11@hotmail.com',
    url='',
    license='Izzy Map App',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
