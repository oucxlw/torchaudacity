from setuptools import setup


with open('README.md') as file:
    long_description = file.read()


setup(
    name='torchaudacity',
    description='',
    version='0.0.1',
    author='Hugo Flores Garcia',
    author_email='hf01049@georgiasouthern.edu',
    url='https://github.com/hugofloresgarcia/torchaudacity',
    install_requires=[
        'torch',
    ],
    packages=['torchaudacity'],
    package_data={'torchaudacity': ['assets/*']},
    include_package_data=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[],
    classifiers=['License :: OSI Approved :: MIT License'],
    license='MIT')