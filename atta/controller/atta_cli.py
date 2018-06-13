import atta.analyzer.generic as ag
import click


@click.command()
@click.option('--readcsv', default="data.csv", help='read csv format data')
def main(readcsv):
    print("Lets analyze something.")
    ag.go(readcsv)


if __name__ == '__main__':
    main()
