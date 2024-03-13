from django.shortcuts import render, redirect

from .forms import QuestionFormFirst, QuestionFormSecond
from .models import QForm


def first_form_view(request):
    if request.method == 'POST':
        form = QuestionFormFirst(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            company_name = form.cleaned_data['company_name']
            prop_type = form.cleaned_data['prop_type']
            request.session['email'] = email
            request.session['company_name'] = company_name
            request.session['prop_type'] = prop_type
            return redirect('second_form_view')
    else:
        form = QuestionFormFirst()
    return render(request, 'first_form.html', {'form': form})


def second_form_view(request):
    email = request.session['email']
    company_name = request.session['company_name']
    prop_type = request.session['prop_type']

    if request.method == 'POST':
        form = QuestionFormSecond(request.POST)
        if form.is_valid():
            form.instance.email = email
            form.instance.company_name = company_name
            form.instance.prop_type = prop_type
            form.save()
            return redirect('success_view')
    else:
        form = QuestionFormSecond(
            initial={
                'email': email,
                'company_name': company_name,
                'prop_type': prop_type
                }
            )
    return render(request, 'second_form.html', {'form': form})


def success_view(request):
    form_ret = QForm.objects.last()
    context = {
        'form_data': form_ret
    }
    return render(request, 'success.html', context=context)
