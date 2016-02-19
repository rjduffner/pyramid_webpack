from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_webpack',
    'waitress',
    ]

setup(name='helloworld',
      version='0.0',
      description='helloworld',
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="helloworld",
      entry_points="""\
      [paste.app_factory]
      main = helloworld:main
      """,
      )
