import click
import os
import hdf5_exdir_converter


@click.command()
@click.help_option('-h', '--help')
@click.argument("filename")
@click.option("--target",
              "-t",
              type=click.STRING,
              help="target filename (optional)",
              required=False)
def exdir2hdf(filename, target=None):
    # TODO: add option for force convert if target exists

    if not filename.endswith(".exdir"):
        raise NameError("filename should have extension `.exdir`")

    filepath, file_extension = os.path.splitext(filename)
    target = target or filepath+".hdf5"

    if not target.endswith(".hdf5"):
        raise NameError("target filename should have extension `.hdf5`")
    if os.path.exists(target):
        raise FileExistsError("target already exists: {}".format(target))

    hdf5_exdir_converter.convert(src_path=filename,
                                 target_path=target)


@click.command()
@click.help_option('-h', '--help')
@click.argument("filename")
@click.option("--target",
              "-t",
              type=click.STRING,
              help="target filename (optional)",
              required=False)
def hdf2exdir(filename, target=None):
    # TODO: add option for force convert if target exists

    if not filename.endswith(".hdf5"):
        raise NameError("filename should have extension `.hdf5`")

    filepath, file_extension = os.path.splitext(filename)
    target = target or filepath+".exdir"

    if not target.endswith(".exdir"):
        raise NameError("target filename should have extension `.exdir`")
    if os.path.exists(target):
        raise FileExistsError("target already exists: {}".format(target))

    hdf5_exdir_converter.convert(src_path=filename,
                                 target_path=target)
