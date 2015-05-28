from distutils.core import setup

setup(
    name='python-package-example',
    version='0.1',
    packages=['myPackage'],
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/BillMills/pythonPackageLesson',
    author='Bill Mills',
    author_email='myemail@example.com'
)
