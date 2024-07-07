from setuptools import setup, find_packages

setup(
    name='inferctl',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'ultralytics',
        'torch',
        'torchvision',
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'inferctl=inferctl:main'
        ]
    },
    author='Arnab',
    author_email='m22cs053@iitj.ac.in',
    description='A CLI app for model inference',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arnabphoenix', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
