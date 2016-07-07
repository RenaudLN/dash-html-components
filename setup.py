from setuptools import setup

setup(
    name='dash_html_components',
    version='0.1.1',
    author='plotly',
    packages=['dash_html_components'],
    package_data={'dash_html_components': ['../lib/metadata.json']},
    license='MIT',
    description='Dash UI component suite',
    install_requires=['flask', 'plotly', 'flask-cors', 'dash.ly']
)