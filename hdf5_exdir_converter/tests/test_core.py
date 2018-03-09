import pytest
import h5py
import exdir
import hdf5_exdir_converter


def _generate_data(src):
    import numpy as np

    time = np.linspace(0, 100, 101)
    voltage_1 = np.sin(time)
    voltage_2 = np.sin(time) + 10

    f = src
    f.attrs['description'] = "This is a mock experiment with voltage values over time"

    dset_time_0 = f.create_dataset("time", data=time)
    dset_time_0.attrs['unit'] = "ms"

    dset_voltage_0 = f.create_dataset("voltage", data=voltage_1)
    dset_voltage_0.attrs['unit'] = "mV"

    # Creating group and datasets for experiment 1
    grp_1 = f.create_group("experiment_1")

    dset_time_1 = grp_1.create_dataset("time", data=time)
    dset_time_1.attrs['unit'] = "ms"

    dset_voltage_1 = grp_1.create_dataset("voltage", data=voltage_1)
    dset_voltage_1.attrs['unit'] = "mV"

    # Creating group and datasets for experiment 2
    grp_2 = f.create_group("experiment_2")

    dset_time_2 = grp_2.create_dataset("time", data=time)
    dset_time_2.attrs['unit'] = "ms"

    dset_voltage_2 = grp_2.create_dataset("voltage", data=voltage_2)
    dset_voltage_2.attrs['unit'] = "mV"

    # Creating group and subgroup for experiment 3
    grp_3 = f.create_group("experiment_invalid")

    # Creating and accessing a subgroup
    grp_4 = grp_3.create_group("subgroup")
    dset_time_4 = grp_4.create_dataset("time", data=time)


def assert_files(f_ex, f_h5):
    assert_attributes(f_ex.attrs, f_h5.attrs)

    for n, m in zip(f_ex, f_h5):
        assert n == m
        is_grp = isinstance(f_ex[n], exdir.core.Group)
        is_dset = isinstance(f_ex[n], exdir.core.Dataset)

        assert is_grp == isinstance(f_h5[n], h5py.Group)
        assert is_dset == isinstance(f_h5[n], h5py.Dataset)

        if is_grp:
            assert_files(f_ex[n], f_h5[n])

        elif is_dset:
            assert_datasets(f_ex[n], f_h5[n])


def assert_attributes(attr_ex, attr_h5):
    assert set(attr_ex.keys()) == set(attr_h5.keys())
    for key, value in dict(attr_ex).items():
        assert attr_h5[key] == value


def assert_datasets(dset_ex, dset_h5):
    # TODO: fix unit
    assert_attributes(dset_ex.attrs, dset_h5.attrs)
    assert all(dset_ex.value == dset_h5.value)


def test_exdir_to_hdf5(setup_teardown_exdir, setup_teardown_hdf5):
    f_ex = exdir.File(setup_teardown_exdir[1], 'w')
    assert f_ex

    _generate_data(f_ex)
    f_ex.close()

    hdf5_exdir_converter.convert(src_path=str(setup_teardown_exdir[1]),
                                 target_path=str(setup_teardown_hdf5[1]))

    f_h5 = h5py.File(setup_teardown_hdf5[1], 'r')
    f_ex = exdir.File(setup_teardown_exdir[1], 'r')

    assert_files(f_ex, f_h5)


def test_hdf5_to_exdir(setup_teardown_exdir, setup_teardown_hdf5):
    f_h5 = h5py.File(setup_teardown_hdf5[1], 'w')
    assert f_h5

    _generate_data(f_h5)
    f_h5.close()

    hdf5_exdir_converter.convert(src_path=str(setup_teardown_hdf5[1]),
                                 target_path=str(setup_teardown_exdir[1]))

    f_h5 = h5py.File(setup_teardown_hdf5[1], 'r')
    f_ex = exdir.File(setup_teardown_exdir[1], 'r')

    assert_files(f_ex, f_h5)
