"""
Flask-Bitcoinrpc
-------------

Bitcoin RPC client for Flask
"""
from setuptools import setup


setup(
    name='Flask-Bitcoinrpc',
    version='0.1',
    url='https://github.com/OneDevGuy/flask-bitcoinrpc',
    license='BSD',
    author='Trevor Johnson',
    description='Bitcoin RPC client for Flask, based on the Python module slick-bitcoinrpc',
    packages=['flask-bitcoinrpc'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'slick-bitcoinrpc>=0.1.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
