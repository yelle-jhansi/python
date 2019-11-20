from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dataapp.models import dataworkz
from django.db.models import Avg, Max, Min, Sum
import datetime
import requests
from django.utils import timezone
from django.db.models import F
from django.db import connection
import dateutil.parser
# import matplotlib.pyplot as plt
# import numpy as np

# Create your views here.

URL= 'http://adunits.datawrkz.com/production/interview/data.json'




class LoadJosnData(APIView):
    def get(self,request):
        url = requests.get(URL)
        content = url.content
        decode_binary = eval(content.decode('ascii'))
        for each in decode_binary:
            dataworkz.objects.create(date=datetime.datetime.strptime(each.get('Date'),'%d-%b-%Y'),opening=each.get('Open'),\
                high=each.get('High'),low=each.get('Low'),\
                closing=each.get('Close'),shares=each.get('Shares Traded'),turnover=each.get('Turnover (Rs. Cr)'))
        return Response({"status":True,"message":'data saved'})

class OrmQueries(APIView):
    def get_date(self,date):
        """
        Function to get custom formated date .
        :returns: Josn-- the return code.
        :param name: date.
        :type name: object.
        """
        
        today_date = timezone.now()
        if date:
            date_list = date.split('/')
            today_date =today_date.replace(day=int(date_list[0]),month=int(date_list[1]),year=int(date_list[2]))
        return today_date

    def get(self,request):

        start_date = self.get_date(request.GET.get('start_date'))
        end_date = self.get_date(request.GET.get('end_date'))


        #task1
        all_records = dataworkz.objects.all().values()

        #task2
        abc = dataworkz.objects.filter(date__gte=start_date,date__lte=end_date)
        stale_activities = abc.filter(opening__gte=F('closing')).values()
        
        #task3
        turnover_avg = dataworkz.objects.filter(date__gte=start_date,date__lte=end_date).aggregate(Avg('turnover')).get('turnover__avg')
    
        #task4
        average_difference = dataworkz.objects.all().aggregate(average_difference=Avg(F('high') - F('low'))).get('average_difference')

        #task5
        truncate_date = connection.ops.date_trunc_sql('month', 'date')
        qs = dataworkz.objects.extra({'month':truncate_date})
        data = qs.values('month').annotate(Avg('opening'),Avg('closing'))
        opening_avg = []
        for each in data:
            d={}
            d['month'] = dateutil.parser.parse(each.get('month')).strftime("%Y-%m")
            d['open_avg'] = each.get('opening__avg')
            d['close_avg'] = each.get('closing__avg')
            opening_avg.append(d)


        #task6
        truncate_date = connection.ops.date_trunc_sql('day', 'date')
        qs = dataworkz.objects.extra({'day':truncate_date})
        data = qs.values('day').annotate(Avg('turnover'))
        opening_avg = []
        for each in data:
            d={}
            d['day'] = each.get('day')
            d['turnover_avg'] = each.get('turnover__avg')
            opening_avg.append(d)
        
        return Response({'all_records':opening_avg})