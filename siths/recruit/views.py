from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import *

# Create your views here.

#испытание для рекрута
def Tasks(request):
    if request.method == 'POST':
        recruit = request.session['recruit_id']
        req = TestTaskForm(recruit, data=request.POST)
        if req.is_valid():
            req.save()
            del request.session['recruit_id']
            return HttpResponseRedirect('/')
    return render(request, 'questions.html',
                  {
                      'form': TestTaskForm(),
                      'actionPath': request.path
                  })

#форма для рекрута
def recruit(request):
    if request.method == 'POST':
        recruitInfo = RecruitInfoForm(request.POST)
        if recruitInfo.is_valid():
            recruit = recruitInfo.save()
            request.session['recruit_id'] = recruit.id
            return HttpResponseRedirect('/questions')
    form = RecruitInfoForm()
    return render(request, 'recruit.html', {
        'actionPath': request.path,
        'form': form
    })


#форма для Ситха
def siths(request):
    #Выбор ситха из списка 
    form = SithChoiceModel()
    template = 'form_choice_Sith.html'
    method = 'GET'
    
    if request.method == 'POST':
        asd = BadHack(request.POST)
        if asd.is_valid():
            val = asd.cleaned_data.get("btn")
            if val == 'accept':
                #как отправить уведомление без рабочего почтового сервера? 
                recruit = RecruitModel.objects.get(
                    id=request.session['recruit_id'])
                recruit.handOfShadow = SithModel.objects.get(
                    id=request.session['sith_id'])
                recruit.save()

        del request.session['recruit_id']
        return HttpResponseRedirect(request.path)

    #Отображение рекрутов не являющиеся "Рукой Тени"
    if 'sith_id' in request.GET:
        request.session['sith_id'] = request.GET['sith_id']
        form = RecruitChoiceModel()
    #формирование ответов рекрута для оценки Ситхом
    if 'recruit_id' in request.GET:
        request.session['recruit_id'] = request.GET['recruit_id']
        answers = RecruitAnswerModel.objects.filter(
            recruit=request.session['recruit_id'])
        template = 'form_answers_show.html'
        method = 'POST'
        form = {}
        for i in range(len(answers)):
            form[str(answers[i].quetion.question)
                 ] = 'True' if answers[i].answer else 'False'

    return render(request, 'siths_base.html',
                  {
                      'actionPath': request.path,
                      'templ': template,
                      'form': form,
                      'method': method
                  })
