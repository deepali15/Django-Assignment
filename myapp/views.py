from django.http.response import HttpResponse
from Assignment.settings import STATIC_FILE_JSON
from django.shortcuts import render
from .forms import InputForm
from datetime import timedelta, datetime
import json
import os
from operator import itemgetter

# Create your views here.


def index(request):
    context = {}
    context['form'] = InputForm()
    if request.GET:
        temp = request.GET['start_date']
        print(type(temp))
    return render(request, "home.html", context)

def question1(request):
    if request.method == 'POST':
        res_form = InputForm(request.POST)

        if res_form.is_valid():
            starttime = res_form.cleaned_data['start_time']
            endtime = res_form.cleaned_data['end_time']

            iststarttime = str(starttime + timedelta(hours=5, minutes=30))
            istendtime = str(endtime + timedelta(hours=5, minutes=30))

            stime = datetime.strptime(iststarttime[:19], "%Y-%m-%d %H:%M:%S")
            etime = datetime.strptime(istendtime[:19], "%Y-%m-%d %H:%M:%S")
            filepath = os.path.join(STATIC_FILE_JSON, "sample_jason_1.json")
            f = open(filepath)

            data = json.load(f)

            shfitAstart = datetime.strptime("06:00:00", "%H:%M:%S").time()
            shfitBstart = datetime.strptime("14:00:00", "%H:%M:%S").time()
            shfitCstart = datetime.strptime("20:00:00", "%H:%M:%S").time()
            shfitAend = datetime.strptime("14:00:00", "%H:%M:%S").time()
            shfitBend = datetime.strptime("20:00:00", "%H:%M:%S").time()
            shfitCend = datetime.strptime("06:00:00", "%H:%M:%S").time()

            dictproA = {
                "production_A_count": 0, "production_B_count": 0,
            }
            dictproB = {
                "production_A_count": 0, "production_B_count": 0,
            }
            dictproC = {
                "production_A_count": 0, "production_B_count": 0,
            }
            resuldct = {
                "shiftA": dictproA,
                "shiftB": dictproB,
                "shiftC": dictproC,
            }
            for i in data:
                intime = i.get('time')
                itime = datetime.strptime(intime, "%Y-%m-%d %H:%M:%S")
                if stime <= itime <= etime:

                    if shfitAstart <= itime.time() < shfitAend:
                        if i.get("production_A"):
                            dictproA["production_A_count"] += 1
                            resuldct["shiftA"] = dictproA
                        if i.get('production_B'):
                            dictproA["production_B_count"] += 1
                            resuldct["shiftA"] = dictproA
                    if shfitBstart <= itime.time() < shfitBend:
                        if i.get("production_A"):
                            dictproB["production_A_count"] += 1
                            resuldct["shiftB"] = dictproB
                        if i.get('production_B'):
                            dictproB["production_B_count"] += 1
                            resuldct["shiftB"] = dictproB
                    if shfitCstart <= itime.time() < shfitCend:
                        if i.get("production_A"):
                            dictproC["production_A_count"] += 1
                            resuldct["shiftC"] = dictproA
                        if i.get('production_B'):
                            dictproC["production_B_count"] += 1
                            resuldct["shiftC"] = dictproC
            f.close()

    return HttpResponse(json.dumps(resuldct), content_type='application/json ; charset=utf8')


def question2(request):
    if request.method == 'POST':
        res_form = InputForm(request.POST)

        if res_form.is_valid():
            starttime = res_form.cleaned_data['start_time']
            endtime = res_form.cleaned_data['end_time']

            iststarttime = str(starttime + timedelta(hours=5, minutes=30))
            istendtime = str(endtime + timedelta(hours=5, minutes=30))

            stime = datetime.strptime(iststarttime[:19], "%Y-%m-%d %H:%M:%S")
            etime = datetime.strptime(istendtime[:19], "%Y-%m-%d %H:%M:%S")
            filepath = os.path.join(STATIC_FILE_JSON, "sample_jason_2.json")
            f = open(filepath)

            data = json.load(f)

            resuldct = {
                "runtime": "",
                "downtime": "",
                "utilisation": 0
            }
            runtime = 0
            downtime = 0

            for i in data:
                intime = i.get('time')
                itime = datetime.strptime(intime, "%Y-%m-%d %H:%M:%S")
                diff = 0
                iruntime = i.get('runtime')

                idowntime = i.get('downtime')
                if stime <= itime <= etime:
                    if iruntime > 1021:
                        diff = iruntime - 1021
                        idowntime = idowntime + diff
                    runtime = runtime + iruntime
                    downtime = downtime + idowntime

            utilization = (runtime / (runtime + downtime)) * 100
            runt = timedelta(seconds=runtime)
            downt = timedelta(seconds=downtime)
            resuldct["runtime"] = str(runt)
            resuldct["downtime"] = str(downt)
            resuldct["utilisation"] = round(utilization, 2)

            f.close()

    return HttpResponse(json.dumps(resuldct), content_type='application/json ; charset=utf8')


def question3(request):
    if request.method == 'POST':
        res_form = InputForm(request.POST)

        if res_form.is_valid():
            starttime = res_form.cleaned_data['start_time']
            endtime = res_form.cleaned_data['end_time']

            iststarttime = str(starttime + timedelta(hours=5, minutes=30))
            istendtime = str(endtime + timedelta(hours=5, minutes=30))

            stime = datetime.strptime(iststarttime[:19], "%Y-%m-%d %H:%M:%S")
            etime = datetime.strptime(istendtime[:19], "%Y-%m-%d %H:%M:%S")

            filepath = os.path.join(STATIC_FILE_JSON, "sample_jason_3.json")
            f = open(filepath)
            data = json.load(f)
            resuldct = []
            lst = []
            for i in data:
                intime = i.get('time')
                itime = datetime.strptime(intime, "%Y-%m-%d %H:%M:%S")

                if stime <= itime <= etime:
                    state = i.get('state')
                    belt1 = i.get('belt1')
                    belt2 = i.get('belt2')
                    inid = i.get('id')
                    inputid = int(inid[2:])
                    if state:
                        belt1 = 0
                    else:
                        belt2 = 0
                    if inputid not in lst:
                        lstdict = {
                            "id": inputid,
                            "avg_belt1": belt1,
                            "avg_belt2": belt2
                        }
                        lst.append(inputid)
                        resuldct.append(lstdict)
                    else:
                        for ele in resuldct:

                            if ele['id'] == inputid:
                                ele['avg_belt1'] += belt1
                                ele['avg_belt2'] += belt2

            for dct in resuldct:
                dct['avg_belt1'] = int(dct['avg_belt1']/2)
                dct['avg_belt2'] = int(dct['avg_belt2'] / 2)

        f.close()
        returnlist = sorted(resuldct, key=itemgetter('id'))

    return HttpResponse(json.dumps(returnlist), content_type='application/json ; charset=utf8')
