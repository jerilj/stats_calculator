FROM python:3

ADD . .

CMD [ "python", "-m","unittest","discover","-v","test" ]