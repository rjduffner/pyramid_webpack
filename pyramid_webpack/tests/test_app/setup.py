from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress',
    ]

setup(name='test_app',
      version='0.0',
      description='test_app',
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
      test_suite="test_app",
      entry_points="""\
      [paste.app_factory]
      main = test_app:main
      """,
      )
