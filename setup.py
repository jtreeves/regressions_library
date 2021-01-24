from setuptools import setup, find_packages

setup(
    name='regressions',
    version='1.0',
    url='https://github.com/jtreeves/regressions_library',
    license='MIT',
    author='Jackson Reeves',
    author_email='jr@jacksonreeves.com',
    description='Generate regression models from data',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['nose>=1.0', 'numpy'],
    test_suite='nose.collector'
)