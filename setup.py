from setuptools import setup


setup(
    name='pyiplocation',
    version='0.1',
    license='MIT',
    description= "A package for geolocating IPS",
    long_description= "A template for publishing python packages",
    long_description_content_type= "text/markdown",
    author="gugu256",
    author_email='gugu256@mail.com',
    url='https://github.com/gugu256/gugu256',
    keywords='example project',
    install_requires=[
          'requests',
      ],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)

