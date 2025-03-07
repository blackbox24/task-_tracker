FROM python:3.8-slim

WORKDIR /app

COPY . .

WORKDIR /app/scripts 

RUN chmod +x ./task-cli.bash 

ENV PATH="/app/scripts:$PATH"

ENTRYPOINT ["task-cli.bash"]