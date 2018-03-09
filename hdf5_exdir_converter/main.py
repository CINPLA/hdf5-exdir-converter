import click


@click.command()
@click.help_option('-h', '--help')
@click.option("--source",
              "-s",
              type=click.STRING,
              help="source filename",
              required=True)
@click.option("--target",
              "-t",
              type=click.STRING,
              help="target filename",
              required=True)
def cli(src, target):
    import hdf5_exdir_converter
    hdf5_exdir_converter.convert(src_path=src,
                                 target_path=target)


def main():
    cli()

if __name__ == "__main__":
    sys.exit(main())
