FROM ubuntu:14.04
# install cowsay, move "default.cow" so we can overwrite"
RUN apt-get update && apt-get install -y cowsay --no-install-recommends && rm -rf /var/lib/apt/lists/* \
&& mv /usr/share/cowsay/cows/default.cow /usr/share/cowsay/cows/orig-default.cow 
# "cowsay" installs to /usr/games
RUN mkdir -p /usr/share/cowsay/cows/
ENV PATH $PATH:/usr/games
ADD ./stormtrooper.cow /usr/share/cowsay/
ADD ./SW_Quotes.dat /usr/games/fortunes/
# install fortune
RUN apt-get -y update && apt-get install -y fortunes
RUN ln -sv /usr/share/cowsay/stormtrooper.cow /usr/share/cowsay/cows/default.cow
CMD /usr/games/fortune -a | cowsay
