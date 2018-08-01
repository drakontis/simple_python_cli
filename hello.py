import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', multiple=True, default='', help='Who are you?')
@click.password_option()
@click.argument('country')
def cli(verbose, name, password, country):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello {0}".format(country))
    for n in name:
        click.echo('Bye {0}'.format(n))
    click.echo('We received {0} as password. (I print password for testing purposes. :) )'.format(password))
