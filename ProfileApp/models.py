from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=6, default='',primary_key=True)
    series = models.CharField(max_length=100,default='')
    bodyTypes = models.CharField(max_length=100,default='')
    color = models.CharField(max_length=100,default='')
    system = models.CharField(max_length=100,default='')
    net = models.IntegerField(default=0.00)

    def pSeries(self):
        if self.series == 'Series i':
            pSeries = 1000000
        elif self.series == 'Series X':
            pSeries = 9000000
        elif self.series == 'Series M':
            pSeries = 7000000
        elif self.series == 'Series 7':
            pSeries = 6000000
        elif self.series == 'Series Concept Cars':
            pSeries = 5000000
        else:#Brochure
            pSeries = 4000000
        return pSeries

    def pBodyTypes(self):
        if self.bodyTypes == 'Coupe':
            bodyTypes = 1800000
        elif self.bodyTypes == 'Convertible':
            bodyTypes = 1700000
        elif self.bodyTypes == 'Sedan':
            bodyTypes = 1600000
        elif self.bodyTypes == 'Sport Activity Coupe':
            bodyTypes = 1500000
        elif self.bodyTypes == 'Sport Activity Vehicle':
            bodyTypes = 1400000
        elif self.bodyTypes == 'Roadster':
            bodyTypes = 1300000
        elif self.bodyTypes == 'Gran Coupe':
            bodyTypes = 1200000
        else:#Gran Turismo
            bodyTypes = 1100000
        return bodyTypes

    def pSystem(self):
        if self.system == 'Full-Electrlc':
            pSystem = 350000
        elif self.system == 'Diesel':
            pSystem = 400000
        elif self.system == 'Gasoline':
            pSystem = 450000
        else:#Plug-In Hybri
            pSystem = 500000
        return pSystem

    def pSum(self):
        pSum = self.pSeries()+ \
               self.pBodyTypes()+ \
               self.pSystem()+\
               self.net
        return pSum

    def pDiscount(self):
        if self.pSum() < 15000000:
            pDiscount = self.pSum()*15/100
        elif self.pSum() < 25000000:
            pDiscount = self.pSum()*25/100
        else:
            pDiscount = self.pSum()*35/100
        return  pDiscount

    def pTotal(self):
        pTotal = self.pSum() - self.pDiscount()
        return pTotal

# class Categor(models.Model):
#     name = models.charField(max_length=50,default='')
#     name = models.charField(max_length=200, default='')
#     def __str__(self):
#         return str(self.id) +":"+self . name +"."+self.desc
#
# class Product(models.Model):
#     pid = models.CharField(max_length=13,primary_key=True, default='')
#     name = models.CharField(max_length=50, default='')
#     brand = models.CharField(max_length=30, default='')
#     price = models.FileField(max_length=0.00)
#     net = models.ImageField(default=0)
#     category = models.ForeignKey(Categor, on_delete=models.CASCADE,default=None)
#     def __str__(self):
#         return self.pid +":"+self.name + ":" +self.brand +":" +str(self.price)+ ":" +str(self.price)+":"+\
#                str(self.net)+":"+ self.category.name
#
# class Devision(models.Model):
#     did = models.CharField(max_length=5,primary_key=True,default='')
#     name = models.CharField(max_length=50,default='')
#     location = models.CharField(max_length=50,default='')
#     def __str__(self):
#         return self.did+','+self.name+','+self.location
# import datetime
# class Employee(models.Model):
#     eid = models.CharField(max_length=13,primary_key=True,default='')
#     name = models.CharField(max_length=35,default='')
#     surname = models.CharField(max_length=35,default='')
#     birthday = models.DateField(default=datetime.date.today())
#     gender = models.BooleanField(default=True)
#     saraly = models.FloatField(default=15000.00)
#     devision = models.ForeignKey(Devision, on_delete=models.CASCADE,default=None)
#     def __str__(self):
#             return  self.eid+ ":"+ self.name+":"+self.surname



