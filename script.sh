#!/bin/bash
#-------------install everything, including python-pip  --------
sudo yum -y install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel python-pip
#----------------------upgrade  --------------------------------
sudo pip install --upgrade
#----------------------take pyenv-installer  -------------------

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#----------------------add strings to .bashrc  -----------------
cat <<EOF >> ~/.bashrc
export PATH="/home/$USER/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF
#---------------------- make source  ----------------------------
source ~/.bashrc
#---------------  install versions  2.7.2 and 3.7.2--------------
pyenv install 2.7.2
pyenv install 3.7.2
pyenv global 3.7.2
#---------------  install virtualenv-----------------------------
sudo pip install virtualenv
#---------------  install virtualenv-----------------------------
pyenv virtualenv 2.7.2 pyvirtenv_2_7
pyenv virtualenv 3.7.2 pyvirtenv_3_7
#------------------------- activate -----------------------------
pyenv activate pyvirtenv_3_7
