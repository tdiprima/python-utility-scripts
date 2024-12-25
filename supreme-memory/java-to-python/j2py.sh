#!/usr/bin/env bash
# https://github.com/natural/java2python/

# We need the ANTLR Python runtime before we can install java2python
wget http://www.antlr3.org/download/antlr-3.1.3.tar.gz
tar xfz antlr-3.1.3.tar.gz
cd antlr-3.1.3/runtime/Python/ || exit
python setup.py install

# Install java2python
wget https://github.com/downloads/natural/java2python/java2python-0.5.1.tar.gz
tar xfz java2python-0.5.1.tar.gz
cd java2python-0.5.1 || exit
sudo python setup.py install

j2py HelloWorld.java
