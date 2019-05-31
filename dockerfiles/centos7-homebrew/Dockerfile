FROM centos:7

RUN yum groupinstall -y 'Development Tools' && \
    yum install -y curl file git && \
    yum install -y which

# https://docs.brew.sh/Homebrew-on-Linux#fedora-centos-or-red-hat 
# に書いてなかったが、which が必要。
# Fedora の場合は、
# `yum install libxcrypt-compat`  needed by Fedora 30 and up
# らしい。

# user1 で実験
RUN useradd --create-home user1
WORKDIR /home/user1
USER user1

# Homebrew 導入
RUN export USER=`whoami` && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

# PATH の設定
RUN echo "eval \$(~/.linuxbrew/bin/brew shellenv)" >>~/.bashrc
