from setuptools import setup, find_packages

setup(
    name='forpay_client',
    version='1.0.0',
    description=(
        'sdk for forpay system'
    ),
    long_description=open('README.rst').read(),
    author='hacfox',
    author_email='zz.hacfox@gmail.com',
    maintainer='hacfox',
    maintainer_email='zz.hacfox@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["python"],
    url='<项目的网址，我一般都是github的url>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
