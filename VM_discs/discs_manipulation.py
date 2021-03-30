from blkinfo import BlkDiskInfo


class Discs:
    @staticmethod
    def get_discs():
        """b = BlkDiskInfo()
        all_discs = b.get_disks()
        table_keys = ["name", "size", "mountpoint"]
        clear_discs = []
        for disc in all_discs:
            temporal_dict = {}
            for key in table_keys:
                if key == 'mountpoint' and disc[key] == '':
                    temporal_dict[key] = '-'
                else:
                    temporal_dict[key] = disc[key]
            clear_discs.append(temporal_dict)

        del all_discs
        return clear_discs"""
        clear_discs = [{'name': 'sda', 'size': '10737418240', 'mountpoint': '-'},
                       {'name': 'sr0', 'size': '1073741312', 'mountpoint': '-'},
                       {'name': 'sr1', 'size': '1073741312', 'mountpoint': '-'}]
        return clear_discs

    def mount_disk(self):
        pass

    def unmount_disk(self):
        pass

    def format_disk(self):
        pass
