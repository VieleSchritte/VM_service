import os


class Discs:
    @staticmethod
    def subdirs_handling(line):
        new_disc = ''
        for letter in line[0]:
            if letter.isdigit() or letter.isalpha():
                new_disc += letter
        return new_disc

    @staticmethod
    def get_disc_info_dict(line):
        disc_info_dict = {"name": line[0], "size": line[3]}
        if len(line) < 7:
            disc_info_dict["mountpoint"] = ''
        else:
            disc_info_dict["mountpoint"] = line[6]
        return disc_info_dict

    @staticmethod
    def lsblk_out_proc(lsblk_out):
        d = Discs()
        all_discs, prev_disc = [], ''
        for line in lsblk_out:
            line = line.strip().split()
            if line[0] == "NAME":
                continue
            if line[0][0].isalpha():
                prev_disc = line[0]
            else:
                new_disc = d.subdirs_handling(line)
                line[0] = prev_disc + '/' + new_disc
            all_discs.append(d.get_disc_info_dict(line))
        return all_discs

    @staticmethod
    def get_discs():
        os.system('mkdir tmp')
        os.system('lsblk >> tmp/lsblk_out.txt')
        with open('tmp/lsblk_out.txt') as lsblk_out:
            d = Discs()
            all_discs = d.lsblk_out_proc(lsblk_out)
        os.system('rm -rf tmp')
        return all_discs

    @staticmethod
    def mount_action(path_to_device, mountpoint):
        mount = 'sudo mount ' + path_to_device + ' ' + mountpoint
        os.system(mount)

    @staticmethod
    def unmount_action(mountpoint):
        unmount = 'sudo unmount ' + mountpoint
        os.system(unmount)

    @staticmethod
    def format_action(path_to_device):
        format_act = 'sudo mkfs -t ext4 ' + path_to_device
        os.system(format_act)
