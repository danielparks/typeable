import click
import sys
import typeable.runs

@click.command()
@click.option('--string', '-s', 'strings', multiple=True)
@click.version_option()
def main(strings):
    qwerty = [
        "`~12345~!@#$%123456qwertasdfgzxcvb\t",
        "67890-=^&*()_+yuiop[]\\{}|hjkl;':\"nm,./<>?"]
    qwerty = [set(chars.lower() + chars.upper()) for chars in qwerty]

    for string in strings:
        print("{:3.0f}% {}".format(
            typeable.runs.fraction(string, qwerty)*100,
            string))
