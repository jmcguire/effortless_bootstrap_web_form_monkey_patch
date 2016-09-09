from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='effortless_bootstrap_web_form_monkey_patch',
      version='0.1',
      description='Patch the old Form classes in web.py to create Bootstrap-compatible forms',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
      ],
      url='http://github.com/jmcguire/effortless_bootstrap_web_form_monkey_patch',
      author='Justin McGuire',
      author_email='jm@landedstar.com',
      keywords='web form bootstrap',
      license='MIT',
      packages=['effortless_bootstrap_web_form_monkey_patch'],
      install_requires=[
        'web',
      ],
      zip_safe=False)
