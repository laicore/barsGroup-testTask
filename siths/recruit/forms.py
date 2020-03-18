from django import forms
from .models import *
import random


class SithChoiceModel(forms.Form):
    sith_id = forms.ModelChoiceField(
        SithModel.objects.all(), label="Выберите себя из списка")

class RecruitChoiceModel(forms.Form):
    recruit_id = forms.ModelChoiceField(
        RecruitModel.objects.filter(handOfShadow=None), label="Выберите рекурта из списка")


class BadHack(forms.Form):
    btn = forms.CharField()

#форма ввода личных данных рекрута
class RecruitInfoForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    age = forms.IntegerField(min_value=1)
    email = forms.EmailField(widget=forms.EmailInput,
                             min_length=5, max_length=100)
    planet = forms.ModelChoiceField(PlanetModel.objects.all())

    def save(self):
        recruit = RecruitModel(**self.cleaned_data)
        recruit.save()
        return recruit

#формирование формы с вопросами из случайного испытания
class TestTaskForm(forms.Form):
    Choices = [('True', True), ('False', False)]

    def __init__(self, recruit=None, **kwargs):
        super(TestTaskForm, self).__init__(**kwargs)
        self.recruit = recruit

        if recruit is None:
            number = random.choice(UniqueOrdenNumberModel.objects.all())
            question = TestTask.objects.filter(uniqueOrdenNumber=number)[:]
            for i in range(len(question)):
                self.fields['question_%i' % question[i].id] = forms.ChoiceField(choices=self.Choices,
                                                                                widget=forms.RadioSelect, 
                                                                                label=question[i].question)

    def save(self):
        #сразу прошу прощения за жесткий парсинг
        recruit = RecruitModel.objects.get(id=self.recruit)
        for i, k in self.data.items():
            t = i.split('_')
            if t[0] == 'question':
                if k == 'True':
                    answ = True
                    t = i.split('_')
                if k == 'False':
                    answ = False
                answer = RecruitAnswerModel(
                    recruit=recruit, quetion_id=int(t[1]), answer=answ)
                answer.save()
