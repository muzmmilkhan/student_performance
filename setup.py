from setuptools import find_packages, setup


def get_requirements(file_name):
    HYPHAN_E_DOT = '-e .'
    with open(file_name,'r') as f:
        l = [i.replace('\n','') for i in f.readlines()]
        if HYPHAN_E_DOT in l:
            l.remove(HYPHAN_E_DOT)
    return l

setup(
    name='student_performance',
    version='0.0.1',
    author='Muzmmil',
    author_email='muzmmil.dba@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)