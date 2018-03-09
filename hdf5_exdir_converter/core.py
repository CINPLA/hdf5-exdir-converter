import exdir
import h5py


def convert_attributes(src, target):
    for key, value in dict(src.attrs).items():
        target.attrs[key] = value


def convert_dataset(src, target):
    convert_attributes(src=src, target=target)
    dset = target.require_dataset(name=src.name,
                                  data=src.value,
                                  shape=src.value.shape,
                                  dtype=src.value.dtype)


def convert_group(src, target, module):
    convert_attributes(src=src, target=target)

    for name, item in src.items():
        if isinstance(item, module.Group):
            grp = target.create_group(name=name)
            convert_group(src=item, target=grp, module=module)

        elif isinstance(item, module.Dataset):
            convert_dataset(src=item, target=target)


def convert(src_path, target_path):
    if src_path.endswith(".exdir"):
        src = exdir.File(src_path, 'r')
        target = h5py.File(target_path, 'w')
        module = exdir.core

    elif src_path.endswith(".hdf5"):
        src = h5py.File(src_path, 'r')
        target = exdir.File(target_path, 'w')
        module = h5py

    convert_attributes(src=src, target=target)
    for name, item in src.items():
        grp = target.create_group(name=name)
        convert_group(src=item, target=grp, module=module)
