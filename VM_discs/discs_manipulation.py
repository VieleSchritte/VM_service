from os import system
import os


class Discs:
    @staticmethod
    def get_discs():
        return [
            {'name': 'loop0', 'size': '55,5M', 'mountpoint': '/snap/core18/1988'},
            {'name': 'loop1', 'size': '219M', 'mountpoint': '/snap/gnome-3-34-1804/66'},
            {'name': 'loop2', 'size': '64,8M', 'mountpoint': '/snap/gtk-common-themes/1514'},
            {'name': 'loop3', 'size': '51M', 'mountpoint': '/snap/snap-store/518'},
            {'name': 'loop4', 'size': '31,1M', 'mountpoint': '/snap/snapd/11036'},
            {'name': 'loop5', 'size': '32,3M', 'mountpoint': '/snap/snapd/11402'},
            {'name': 'loop6', 'size': '55,5M', 'mountpoint': '/snap/core18/1997'},
            {'name': 'sda', 'size': '10G', 'mountpoint': ''},
            {'name': 'sda/sda1', 'size': '512M', 'mountpoint': '/boot/efi'},
            {'name': 'sda/sda2', 'size': '1K', 'mountpoint': ''},
            {'name': 'sda/sda5', 'size': '9,5G', 'mountpoint': '/'},
            {'name': 'sr0', 'size': '1024M', 'mountpoint': ''},
            {'name': 'sr1', 'size': '1024M', 'mountpoint': ''}
        ]
"""        all_discs = []
        os.system('lsblk >> lsblk_out.txt')
        with open ('lsblk_out.txt') as lsblk_out:
            for line in lsblk_out:
                line = line.strip().split()
                if line[0] == "NAME":
                    continue
                temporal_dict = {"name": line[0], "size": line[3]}
                if len(line) < 7:
                    temporal_dict["mountpoint"] = ''
            all_discs.append(temporal_dict)
        return all_discs"""

