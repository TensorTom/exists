# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exists']

package_data = \
{'': ['*']}

install_requires = \
['datafunc>=0.0.4,<0.0.5']

setup_kwargs = {
    'name': 'exists',
    'version': '0.1.0',
    'description': 'Check if a variable or other object exists.',
    'long_description': '# exists\n\nPython module to check if a variable or other object exists.\n\n```python\nfrom exists import exists\n\nmyvar = True\nassert exists(myvar)\n```',
    'author': 'Tom A.',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TensorTom/exists',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
