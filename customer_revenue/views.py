import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, get_list_or_404
from datetime import datetime
from customer_revenue.models import Contact, fist
# from customer_revenue.models import fist
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def finding_type(x):
    # New_Visitor	Other	Returning_Visitor
    if x == 1:
        return [1, 0, 0]
    elif x == 2:
        return [0, 0, 1]
    else:
        return [0, 1, 0]

# Create your views here.


def first(request):
    res = None
    result = ""
    if request.method == 'POST':
        if request.POST.get('pred_button'):

            name = request.POST['Product Name']
            Administrative = request.POST['Administrative']
            Informational = request.POST['Informational']
            ProductRelated = request.POST['ProductRelated']
            BounceRates = request.POST['BounceRates']
            ExitRates = request.POST['ExitRates']
            PageValues = request.POST['PageValues']
            SpecialDay = request.POST['SpecialDay']
            OperatingSystems = request.POST['OperatingSystems']
            Browser = request.POST['Browser']
            Region = request.POST['Region']
            TrafficType = request.POST['TrafficType']
            VisitorType = request.POST['VisitorType']
            weekend = request.POST['weekend']

            # print(name, type(Administrative))
            if name != "":
                try:
                    df = pd.DataFrame(columns=['Administrative_Duration', 'Informational_Duration', 'ProductRelated',
                                               'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay',
                                               'OperatingSystems', 'Browser', 'Region', 'TrafficType',
                                               'Weekend', 'New_Visitor', 'Other', 'Returning_Visitor'])

                    type_visitor = finding_type(VisitorType)
                    df2 = {'Administrative_Duration': float(Administrative),
                           'Informational_Duration': float(Informational),
                           'ProductRelated': float(ProductRelated),
                           'BounceRates': float(BounceRates),
                           'ExitRates': float(ExitRates),
                           'PageValues': float(PageValues),
                           'SpecialDay': float(SpecialDay),
                           'OperatingSystems': int(OperatingSystems),
                           'Browser': int(Browser),
                           'Region': int(Region),
                           'TrafficType': int(TrafficType),
                           'Weekend': int(weekend),
                           'New_Visitor': type_visitor[0], 'Other': type_visitor[1], 'Returning_Visitor': type_visitor[2]}

                    df = df.append(df2, ignore_index=True)
                    import joblib
                    model = joblib.load('customer_revenue/model_save')

                    res = model.predict(df)

                    print(res)
                    if res[0] == 1:
                        result = "True"
                        messages.success(
                            request, f'The customer will generate {result} Revenue ')
                    else:
                        result = "False"
                        messages.success(
                            request, f' The customer will generate {result} Revenue ')
                except:
                    pass

    return render(request, "customer.html", {'result': result})


def finding_type(x):
    # New_Visitor	Other	Returning_Visitor
    if x == 1:
        return [1, 0, 0]
    elif x == 2:
        return [0, 0, 1]
    else:
        return [0, 1, 0]
