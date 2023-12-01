from setuptools import setup

setup(
    name='sunnyday-IP',            # Your package will have this name
    packages=['sunnyday'],      # Name the package again
    version='2.0.0',            # To be increased every time you change your library
    license='MIT',              # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',         # Short description of your library
    author='Ievgen Perederieiev',                # Your name
    author_email='my.test.email@gmail.com',      # Your email
    url='https://example.com',                   # Homepage of your library
    keywords=['weather', 'forecast', 'openweather'],    # Keywords users can search on pypi.com
    install_requires=[                          # Other third-party libs that pip needs to install
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3-Alpha, 4-Beta or 5-Production/Stable" as a current status
        'Intended Audience :: Developers',      # Who is the audience of your library
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Type of license again
        'Programming Language :: Python :: 3.5',    # Python versions that your library supports
        'Programming Language :: Python :: 3.6',    # Python versions that your library supports
        'Programming Language :: Python :: 3.7',    # Python versions that your library supports
        'Programming Language :: Python :: 3.8',    # Python versions that your library supports
        'Programming Language :: Python :: 3.9',    # Python versions that your library supports
        'Programming Language :: Python :: 3.10',    # Python versions that your library supports
        ],
)
