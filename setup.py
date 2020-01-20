from setuptools import setup, find_packages

setup(
    name='forpay_client',
    version='1.0.12',
    description=(
        'Python sdk for Forpay system'
    ),
    author='bozimeile',
    author_email='zz.hacfox@gmail.com',
    maintainer='bozimeile',
    maintainer_email='zz.hacfox@gmail.com',
    license='MIT License',
    packages=find_packages(exclude=[]),
    platforms=["python"],
    url='https://github.com/hacfox/forpay_client.git',
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
