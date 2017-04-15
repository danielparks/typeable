import click
import sys
import typeable.runs

def querty():
    qwerty = [
        "`~12345~!@#$%123456qwertasdfgzxcvb\t",
        "67890-=^&*()_+yuiop[]\\{}|hjkl;':\"nm,./<>?"]
    return [set(chars.lower() + chars.upper()) for chars in qwerty]

@click.group()
@click.version_option()
def main():
    pass

@main.command()
@click.option('--string', '-s', 'strings', multiple=True)
def run_percent(strings):
    hands = querty()
    for string in strings:
        click.echo("{:3.0f}% {}".format(
            typeable.runs.fraction(string, hands)*100,
            string))

@main.command()
@click.option('--string', '-s', 'strings', multiple=True)
def run_count(strings):
    hands = querty()
    for string in strings:
        click.echo("{:2d} {}".format(
            typeable.runs.count(string, hands),
            string))

@main.command()
@click.argument('files', nargs=-1, type=click.File('r'))
@click.option('--maximum-run-percent', '-m', type=click.IntRange(0, 100), default=50)
def filter(files, maximum_run_percent=0.5):
    if not files:
        files = [sys.stdin]
    hands = querty()
    for file in files:
        for line in file:
            line = line.rstrip("\n")
            if typeable.runs.fraction(line, hands)*100 <= maximum_run_percent:
                click.echo(line)
