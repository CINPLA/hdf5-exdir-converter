import click


@click.command()
@click.help_option('-h', '--help')
@click.argument("src",
                type=click.STRING)
@click.argument("target",
                type=click.STRING)
def cli(src, target):
    import hdf5_exdir_converter

    hdf5_exdir_converter.convert(src_path=src,
                                 target_path=target)


def main():
    cli()

if __name__ == "__main__":
    sys.exit(main())
