FROM debian:8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      autoconf \
      build-essential \
      bzip2 \
      gcc \
      g++ \
      git \
      make \
      patch \
      tar \
      wget \
      zlib1g-dev \
      sed \
      libreadline6-dev \
      libglib2.0-0 \
      libxext6 libxext-dev \
      libxrender1 libxrender-dev \
      libsm6 libsm-dev \
      libsmbclient-dev \
      tk-dev \
      libx11-6 libx11-dev \
      # gobject-introspection
      flex \
      # install extra packages for gobject-introspection package
      libffi-dev \
      libssl-dev \
      bison \
      # install packages for hkl
      gtk-doc-tools \
      # need an editor...
      vim \
      # and one for tom...
      emacs && \
	  rm -rf /var/lib/apt/lists/*

# Set the Locale so conda doesn't freak out
# It is roughly this problem: http://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting
# I don't remember exactly where I found this solution, but it took about 2 days of
# intense googling and trial-and-error
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
    apt-get install -y locales -qq && \
	sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen en_US.UTF-8 en_us && \
    dpkg-reconfigure locales

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Add the conda binary folder to the path
ENV PATH /conda/bin:$PATH

# Actually install miniconda
RUN cd && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh --no-verbose && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /conda && \
    rm Miniconda*.sh

RUN apt update
RUN apt -y install libgl1-mesa-glx
RUN pip install --upgrade pip
COPY /docker_ml_base_image/requirements.txt .
RUN pip install -r requirements.txt
COPY /application .

ENV PYTHONPATH="${PYTHONPATH}:/app/application"

WORKDIR /src

CMD ["python3", "app.py"]