FROM python:3.8-slim
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
COPY requirements.txt .

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /app

# copy over requirements
COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip install -r requirements.txt

# copying all files over
COPY . .

# cmd to launch app when container is run
CMD streamlit run picture_perfect   /app.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'
