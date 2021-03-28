from blkinfo import BlkDiskInfo
import json


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
        print('======', clear_discs)
        del all_discs
        return clear_discs"""
        trial_data = [{'name': 'sda', 'size': '10737418240', 'mountpoint': '-'},
                {'name': 'sr0', 'size': '1073741312', 'mountpoint': '-'},
                {'name': 'sr1', 'size': '1073741312', 'mountpoint': '-'}]

        """return json.dumps(trial_data)"""
        return trial_data
