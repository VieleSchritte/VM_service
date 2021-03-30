from os import system
import os


class Discs:
    @staticmethod
    def get_discs():
        all_discs = []
        os.system('mkdir tmp')
        os.system('lsblk >> tmp/lsblk_out.txt')
        with open ('tmp/lsblk_out.txt') as lsblk_out:
            for line in lsblk_out:
                line = line.strip().split()
                if line[0] == "NAME":
                    continue
                temporal_dict = {"name": line[0], "size": line[3]}
                if len(line) < 7:
                    temporal_dict["mountpoint"] = ''
                else:
                    temporal_dict["mountpoint"] = line[6]
                all_discs.append(temporal_dict)
        os.system('rm -rf tmp')
        print(all_discs)
        return all_discs
