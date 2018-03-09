import pytest
import shutil
import os
import h5py
import pathlib
import exdir


def remove(name):
    if name.exists():
        shutil.rmtree(str(name))
    assert not name.exists()


@pytest.fixture
def setup_teardown_exdir(tmpdir):
    testpath = pathlib.Path(tmpdir.strpath)
    testdir = testpath / "exdir_dir"
    testfile = testpath / "test.exdir"

    remove(testpath)

    testpath.mkdir(parents=True)

    yield testpath, testfile, testdir

    # remove(testpath)


@pytest.fixture
def setup_teardown_hdf5(tmpdir):
    testpath = pathlib.Path(tmpdir.strpath)
    testdir = testpath / "hdf5_dir"
    testfile = testpath / "test.hdf5"

    remove(testpath)

    testpath.mkdir(parents=True)

    yield testpath, testfile, testdir

    # remove(testpath)
