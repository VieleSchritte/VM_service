from django.shortcuts import render
from .discs_manipulation import Discs
from django.contrib.auth.decorators import login_required


@login_required
def discs_table(request):
    d = Discs()
    clear_discs = d.get_discs()
    return render(request, 'discs_table.html', {"clear_discs": clear_discs})


def get_action(request):
    d = Discs()
    clear_discs = d.get_discs()
    for disc in clear_discs:
        trial_request = request.GET(disc["name"])
        print(trial_request)
