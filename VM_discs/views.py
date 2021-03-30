from django.shortcuts import render
from .discs_manipulation import Discs
from django.contrib.auth.decorators import login_required


def disc_args_for_view():
    d = Discs()
    all_discs = d.get_discs()
    args = {"all_discs": all_discs}
    return args


@login_required
def discs_table(request):
    args = disc_args_for_view()
    return render(request, 'discs_table.html', args)


def mount_disc(request):
    if request.method == 'POST':
        mountpoint = request.POST.get('mounpoint_name', 0).strip()
        path_to_device = request.POST.get('mount-disc', 0)
        d = Discs()
        d.mount_action(path_to_device, mountpoint)
        args = disc_args_for_view()
        return render(request, 'discs_table.html', args)


def unmount_disc(request):
    if request.method == 'POST':
        mountpoint = request.POST.get('unmount-disc', 0)
        d = Discs()
        d.unmount_action(mountpoint)
        args = disc_args_for_view()
        return render(request, 'discs_table.html', args)


def format_disc(request):
    if request.method == 'POST':
        disc_name = request.POST.get('format-disc', 0)
        d = Discs()
        d.format_action(disc_name)
        args = disc_args_for_view()
        return render(request, 'discs_table.html', args)
