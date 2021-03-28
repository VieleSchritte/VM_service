from django.shortcuts import render
from .discs_manipulation import Discs


def disks_table(request):
    d = Discs()
    clear_discs = d.get_discs()
    return render(request, 'disks_table.html', {{clear_discs}})
