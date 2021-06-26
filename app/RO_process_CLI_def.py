import click
from flask import Flask
from flask.cli import AppGroup

app = Flask(__name__)
user_cli = AppGroup('user')

@user_cli.command('CreateProcess')
@click.argument('serviceID','boot_type')
def CreateProcess(name):
  

app.cli.add_command(user_cli)
#$ flask user create demo