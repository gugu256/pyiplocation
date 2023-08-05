from setuptools import setup


setup(
    name='pyiplocation',
    version='0.3',
    license='MIT',
    description= "A package for geolocating IPs",
    long_description= open("README.md").read(),
    long_description_content_type= "text/markdown",
    project_urls={"Homepage": "https://github.com/gugu256/pyiplocation"},
    author="gugu256",
    author_email='gugu256@mail.com',
    url='https://github.com/gugu256/gugu256',
    keywords='ip location',
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

