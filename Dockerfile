FROM gitpod/workspace-full
USER gitpod
RUN sudo apt-get -y update
RUN sudo apt-get -y dist-upgrade
RUN sudo apt-get -y autoremove
RUN sudo apt-get install -y tmux nano wget nano vim neofetch yakuake
RUN echo "cheese"