from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# from django import forms
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
from datetime import datetime
from users.models import UserModel
from .forms import AccountForm, ValidateAccountForm
# from .ott import ott_gen_func, TOKENS, TOKENS_TIME
from .ott import ott_gen_func
from datetime import datetime

# TOKENS = dict()
# TOKENS_TIME = dict()

@never_cache
def signin_view(request):
    if request.user.is_authenticated: 
        return redirect("users:user_detail_page")
    if "check_user" in request.session:
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print(request.session["check_user"])
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return redirect("signin:validate_account_page", pk=request.session.get("check_user"))
    if request.method == "POST":
        form = AccountForm(request.POST)
        account = UserModel()
        if form.is_valid():
            cd = form.cleaned_data

            account.email = cd["email"]
            account.full_name = cd["fullname"]
            passwd = cd["passwd"]
            confrim_passwd = cd["confrim_passwd"]
            account.age = cd["age"]
            account.sex = request.POST.get("sex")
            account.bio = cd["bio"]

            if passwd == confrim_passwd:
                account.set_password(passwd)
            else:
                return redirect("signin:signin_page")

            if account.sex == None:
                account.sex = "other"

            account._set_user_unique_id()

            # account.save()

            token = ott_gen_func() #################################################################################

            account.tmp_token = str(token)
            account.tmp_token_time = datetime.now()

            account.save()

            # TOKENS.update({str(account.id): str(token)})
            # TOKENS_TIME.update({str(account.id): datetime.now()})

            msg = f"Wite\n\nHeloo {account}.\n\"{token}\" is code to active and validate your account in wite.\n"
            send_mail("Validation Code", msg, "witesmtp@gmail.com",
                      [account.email], False)
            # from django.conf import settings
            # send_mail("Validation Code", msg, f"{settings.EMAIL_HOST_USER}", [str(account.email)], fail_silently=False)

            # TOKENS.update({str(account.id): str(token)})
            # TOKENS_TIME.update({str(account.id): datetime.now()})

            # user = authenticate(
            #     request, email=cd["email"], password=cd["passwd"])
            # if user != None:
            #     login(request, user)


            request.session["check_user"] = account.id
            request.session.set_expiry(300)

            return redirect("signin:validate_account_page", pk=account.id)
            # user = authenticate(request, email=user.email, password=cd["passwd"])
            # login(request, user)
            # return redirect("users:user_detail_page")

    else:
        form = AccountForm()
        account = UserModel()

    context = {
        "form": form,
        "account": account,
    }

    return render(request, "signin/signin.html", context)


@never_cache
def validate_account_view(request, pk):
    if request.user.is_authenticated: 
        return redirect("users:user_detail_page")
    # print(TOKENS)
    user = UserModel.objects.get(id=pk)
    token = user.tmp_token
    # token = TOKENS[str(pk)]
    if request.method == "POST":
        user_tmp_token_time_str = str(user.tmp_token_time).split(".")[0]
        user_tmp_token_time = datetime.strptime(user_tmp_token_time_str, "%Y-%m-%d %H:%M:%S")
        check_time = datetime.now()
        check_time_str = str(check_time).split(".")[0]
        check_time_frmt = datetime.strptime(check_time_str, "%Y-%m-%d %H:%M:%S")
        print(check_time_frmt)
        # time = check_time - datetime.strptime(user.tmp_token_time, "%Y-%m-%d %H:%M:%S")
        # time = check_time - user_tmp_token_time
        time = check_time_frmt - user_tmp_token_time
        time = time.total_seconds()
        # check_time = datetime.now()
        # time = check_time - TOKENS_TIME[str(pk)]
        # time = time.total_seconds()

        if int(time) > 300:
            user.delete()
            return redirect("signin:signin_page")

        # if int(time) > 300:
        #     TOKENS.pop(str(pk))
        #     TOKENS_TIME.pop(str(pk))
        #     user.delete()
        #     return redirect("signin:signin_page")
        form = ValidateAccountForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            code = cd["code"]
            code = int(code)
            passwd = cd["passwd"]

            if not user.check_password(passwd):
                return redirect("signin:signin_page")

            if str(code) == str(token):
                user.is_active = True
                user.save()
                user = authenticate(
                    request, email=user.email, password=cd["passwd"])
                if user != None:
                    if user.is_active:
                        login(request, user)
                        user.tmp_token = None
                        user.tmp_token_time = None
                        user.save()
                        # TOKENS.pop(str(pk))
                        # TOKENS_TIME.pop(str(pk))
                        return redirect("users:user_detail_page")

    else:
        form = ValidateAccountForm()

    context = {
        "form": form,
    }

    return render(request, "signin/validate-user.html", context)

