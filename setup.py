from setuptools import setup

setup(name='jupyterix86',
      version='0.1',
      description='x86 assembly in Jupyter',
      url='http://osdev.me/',
      author='Levente Kurusa',
      author_email='levex@linux.com',
      license='MIT',
      packages=['jupyterix86', 'jupyterix86.kernel'],
      package_data={'': ['support/*.S', 'support/*.sh']},
      zip_safe=False)
