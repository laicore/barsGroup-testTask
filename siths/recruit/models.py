from django.db import models

# Create your models here.


class PlanetModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SithModel(models.Model):
    name = models.CharField(max_length=100)
    learnPlanet = models.ForeignKey(
        PlanetModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class RecruitModel(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(
        PlanetModel, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    email = models.EmailField()
    handOfShadow = models.ForeignKey(SithModel,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name


class UniqueOrdenNumberModel(models.Model):
    uniqueTestNumber = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.uniqueTestNumber)


class TestTask(models.Model):
    uniqueOrdenNumber = models.ForeignKey(
        UniqueOrdenNumberModel, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200)


class RecruitAnswerModel(models.Model):
    recruit = models.ForeignKey(RecruitModel, on_delete=models.CASCADE)
    quetion = models.ForeignKey(TestTask, on_delete=models.SET_NULL, null=True)
    answer = models.BooleanField(default=False)
    def __str__(self):
        return 'True' if self.answer else 'False'
