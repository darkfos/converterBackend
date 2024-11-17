FROM python:3.12
WORKDIR /backend_convert

COPY . ./
RUN pip install -r requirements.txt && sudo apt-get install pandoc && sudo apt-get install texlive && sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-fonts-extra

CMD ["python3", "main.py"]