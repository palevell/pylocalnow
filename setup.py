from setuptools import setup

setup(name='localnow',
      version='1.1.7',
      description='Returns a PyTZ object with the local time & timezone',
      url='https://github.com/palevell/pylocalnow',
      author='Patrick A. Levell',
      author_email='patrick.a.levell@gmail.com',
      license='MIT',
      #packages=['localnow'],
      install_requires=[
            'pytz',
            'tzlocal'
      ],
      scripts=['bin/localnow'],
      zip_safe=False
)

