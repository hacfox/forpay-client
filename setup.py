from setuptools import setup, find_packages

NAME = 'forpay_client'
VERSION = '1.0.15'
AUTHOR = 'bozimeile'
EMAIL = 'zz.hacfox@gmail.com'
URL = 'https://github.com/hacfox/forpay_client.git'
DESCRIPTION = 'The client module of Forpay Python sdk'

# desc_file = open("README.md")
# try:
#     LONG_DESCRIPTION = desc_file.read()
# finally:
#     desc_file.close()
LONG_DESCRIPTION = ('''
# forpay_client
SDK For Forpay  
API Link: [Forpay](https://api.forpay.pro/docs/overview)

## Install

```
pip install forpay-client
```

## Usage

```
client = ForPayClient(app_id='app_id', key_id='key_id', private_key='private_string')
reply, ok = client.get_currencies()
```
## License

MIT © bozimeile
''')

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT License',
    packages=find_packages(exclude=['test*']),
    platforms="any",
    keywords=['forpay', 'forpay-client', 'sdk'],
    url=URL,
    install_requires=[
        'pycryptodome>=3.9.4',
        'requests>=2.22.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ],
)
