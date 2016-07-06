from setuptools import setup
with open('README.rst') as f:
    readme = f.read()
setup(name='TargetProcessClient',
      version='0.1',
      author='Sergey Plokhikh',
      author_email='sergey.plokhikh@iqoption.com',
      license='MIT',
      description='This package allow get user stories and move it on board',
      long_description=readme,
      packages=["target_process"])
