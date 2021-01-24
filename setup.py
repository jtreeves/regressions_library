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
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    zip_safe=False,
    install_requires=['numpy'],
    setup_requires=['nose>=1.0', 'numpy'],
    test_suite='nose.collector'
)