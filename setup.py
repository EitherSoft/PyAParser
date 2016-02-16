try:
    import multiprocessing
except ImportError:
    pass


from setuptools import setup

setup(
    name='PyAParser',
    version='0.1',
    description='Python library for working with AParser API',
    url='https://github.com/kronas/PyAParser',
        
    author='Kronas',
    author_email='kronas.sw@gmail.com',
    license='MIT',

    packages=['aparser'],

    install_requires=[
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe=False,
)
