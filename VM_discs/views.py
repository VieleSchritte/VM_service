from django.shortcuts import render
from .discs_manipulation import Discs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def sign_up(request):
    user_name = request.POST.get('type', 'user_name')
    user_email = request.POST.get('type', 'user_email')
    user_password = request.POST.get('type', 'user_password')
    user = User.objects.create_user(user_name, user_email, user_password)
    print('===========your new user: ', user)


@login_required
def discs_table(request):
    d = Discs()
    clear_discs = d.get_discs()
    return render(request, 'discs_table.html', {"clear_discs": clear_discs})
