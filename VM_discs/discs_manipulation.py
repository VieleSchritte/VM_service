from blkinfo import BlkDiskInfo
import json
import linu


class Discs:
    @staticmethod
    def get_discs():
        b = BlkDiskInfo()
        all_disks = b.get_disks()
        json_output = json.dumps(all_disks)
        print(json_output)
