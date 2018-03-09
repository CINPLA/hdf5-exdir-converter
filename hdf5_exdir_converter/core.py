import exdir
import h5py


def convert_attributes(src, target):
    for key, value in dict(src.attrs).items():
        target.attrs[key] = value


def convert_dataset(src, target):
    convert_attributes(src=src, target=target)
    dset = target.require_dataset(name=src.name.split("/")[-1],
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
        if not target_path.endswith(".hdf5"):
            raise NameError("converting to hdf5: target should have extension .hdf5")

        src = exdir.File(src_path, 'r')
        target = h5py.File(target_path, 'w')
        module = exdir.core

    elif src_path.endswith(".hdf5"):
        if not target_path.endswith(".exdir"):
            raise NameError("converting to exdir: target should have extension .exdir")
        src = h5py.File(src_path, 'r')
        target = exdir.File(target_path, 'w')
        module = h5py

    else:
        raise NameError(
            "src should have extension .hdf5 or .exdir"
        )

    convert_attributes(src=src, target=target)
    for name, item in src.items():
        grp = target.create_group(name=name)
        convert_group(src=item, target=grp, module=module)

    src.close()
    target.close()
