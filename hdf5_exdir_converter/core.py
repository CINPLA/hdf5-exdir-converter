import exdir
import h5py


def convert_attributes(src, target):
    for key, value in dict(src.attrs).items():
        target.attrs[key] = value
    
    
def convert_dataset(src, target):
    convert_attributes(src=src, target=target)
    dset = target.require_dataset(name=src.name, 
                                  data=src.data,
                                  shape=src.data.shape,
                                  dtype=src.data.dtype)
    
    
def convert_group(src, target):
    convert_attributes(src=src, target=target)

    for name, item in src.items():
        if isinstance(item, exdir.core.Group):
            grp = target.create_group(name=name)
            convert_group(src=item, target=grp)
            
        elif isinstance(item, exdir.core.Dataset):
            convert_dataset(src=item, target=target)


def convert(src_file, target):
    # TODO: check filename extension
    # TODO: check type (exdir/hdf5)
    
    convert_attributes(src=src, target=target)
    for name, item in src.items():
        grp = target.create_group(name=name)
        convert_group(src=item, target=grp)
