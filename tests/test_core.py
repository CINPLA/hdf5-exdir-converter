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
    #
    # # Looping through and accessing
    # print("Experiments: ", list(f.keys()))
    # for experiment in f.keys():
    #     if "voltage" in f[experiment]:
    #         print(experiment)
    #         print(f[experiment]["voltage"])
    #         print("First voltage:", f[experiment]["voltage"][0])
    #     else:
    #         print("No voltage values for: {}".format(experiment))

    # Creating and accessing a subgroup
    grp_4 = grp_3.create_group("subgroup")
    dset_time_4 = grp_4.create_dataset("time", data=time)


def test_exdir_to_hdf5(setup_teardown_exdir, setup_teardown_hdf5):
    f_ex = exdir.File(setup_teardown_exdir[1], 'w')
    assert f_ex

    _generate_data(f_ex)
    f_ex.close()

    hdf5_exdir_converter.convert(src_path=str(setup_teardown_exdir[1]),
                                 target_path=str(setup_teardown_hdf5[1]))


@pytest.mark.to_exdir
def test_hdf5_to_exdir(setup_teardown_exdir, setup_teardown_hdf5):
    f_h5 = h5py.File(setup_teardown_hdf5[1], 'w')
    assert f_h5

    _generate_data(f_h5)
    f_h5.close()

    hdf5_exdir_converter.convert(src_path=str(setup_teardown_hdf5[1]),
                                 target_path=str(setup_teardown_exdir[1]))
