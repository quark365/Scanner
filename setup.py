# setup.py

from setuptools import setup, find_packages

setup(
    name='Scanner',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A module to evaluate user input expressions safely.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Adithya Krishna S',
    author_email='quark365microbot@outlook.com',
    url='https://github.com/quark365/Scanner',
    keywords=['input', 'evaluation', 'expression','Scanner'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
