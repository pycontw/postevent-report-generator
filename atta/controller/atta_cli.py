import atta.analyzer.generic as ag
import click


@click.command()
@click.option('--csv', default="data.csv", help='read csv format data')
def main(csv):
    print("Lets analyze something.")
    ag.go(csv)


if __name__ == '__main__':
    main()
