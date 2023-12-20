from jarguments import __author__, __doc__, __license__, __module_name__, __python_version__, __version__

from setuptools import setup

setup(
	name=__module_name__,
	version=__version__,
	description=__doc__,
	long_description=open('README.md', 'r').read(),
	long_description_content_type='text/markdown',
	url=f'https://github.com/{__author__}/{__module_name__}',
	author=__author__,
	include_package_data=True,
	license=__license__,
	packages=[__module_name__],
	package_data={},
	setup_requires=['pytest_runner'],
	python_requires=f'>={__python_version__}',
	scripts=[],
	tests_require=['pytest'],
	entry_points={},
	zip_safe=True,
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
