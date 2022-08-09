from django.shortcuts import render
from firstApp.models import employee_model, manager_model
from django.db.models import Q,Avg,Sum,Min,Max,Count
# Create your views here.
def display_view(request):

    #employee = employee_model.objects.all()#to get all data from the databases

    # TO FILTER RECORDS BASED ON SOME CONDITIONS


    #employee = employee_model.objects.filter(id=1)#to get only one record
    #employee = employee_model.objects.filter(id__exact=14)#to get only one record
    #employee = employee_model.objects.filter(ename__iexact='robert williams')#to get the recordes that maches the ename field of databade table with case-insensitive
    #employee = employee_model.objects.filter(ename__exact='Robert Williams')#to get the recordes that maches the ename field of databade table with case-sensitive
    #employee = employee_model.objects.filter(ename__contains='Ra')#to get the recordes that maches the ename field of databade table that have on in it with case-sensitive
    #employee = employee_model.objects.filter(ename__contains='on')#to get the recordes that maches the ename field of databade table that have on in it with case-insensitive
    #employee = employee_model.objects.filter(id__in=[3,4,5,7])#to get the record that maches the id field of databade table with the elements in the given iteratable(list or tuple)
    #employee = employee_model.objects.filter(esal__gt=15000)#to get the employee records having esal firld greater than 15000
    #employee = employee_model.objects.filter(esal__gte=15000)#to get the employee records having esal firld greater than or equalto 15000
    #employee = employee_model.objects.filter(esal__lt=15000)#to get the employee records having esal firld lesser than 15000
    #employee = employee_model.objects.filter(esal__lte=15000)#to get the employee records having esal firld lesser than or equal to 15000
    #employee = employee_model.objects.filter(ename__startswith='Li')#to get the employee records having ename field starts with the specified with case-sensitive
    #employee = employee_model.objects.filter(ename__istartswith='ma')#to get the employee records having ename field starts with the specified with case-insensitive
    #employee = employee_model.objects.filter(ename__endswith='is')#to get the employee records having ename field ends with the specified with case-sensitive
    #employee = employee_model.objects.filter(ename__iendswith='ON')#to get the employee records having ename field ends with the specified with case-insensitive
    #employee = employee_model.objects.filter(esal__range=(12000,16000))#to get the employee records having esal field between specified

    # TO IMPLEMENT OR QUERIES IN DJANGO ORM (2 ways)

    #employee = employee_model.objects.filter(ename__startswith='D') | employee_model.objects.filter(esal__lt=12000)#to get the employee record having either ename field starts with D or esal field less than 12000
    #employee = employee_model.objects.filter(Q(ename__startswith='D') | Q(esal__lt=12000))#to get the employee record having either ename field starts with D or esal field less than 12000 (using Q mdule)

    # TO IMPLEMENT AND QUERIES IN DJANGO ORM (3 ways)

    #employee = employee_model.objects.filter(ename__startswith='D') & employee_model.objects.filter(esal__lt=12000)#to get the employee record having ename field starts with D and esal field less than 12000
    #employee = employee_model.objects.filter(Q(ename__startswith='D') & Q(esal__lt=12000))#to get the employee record having ename field starts with D and esal field less than 12000(using Q)
    #employee = employee_model.objects.filter(ename__startswith='D',esal__lt=12000)#to get the employee record having ename field starts with D and esal field less than 12000(using ,)

    # TO IMPLEMENT NOT QUERIES IN DJANGO ORM (2 ways)

    #employee = employee_model.objects.exclude(esal__range=[12000,18000])#to get the employee record by excluding the specified
    #employee = employee_model.objects.filter(~Q(esal__range=[12000,18000]))#to get the employee record by excluding the specified

    # TO IMPLEMENT UNION FOR QUERIES OF SAME OR DIFFERENT MODELS

    #employee_1 = employee_model.objects.filter(esal__lt=15000)#to get the employee records having esal field lesser than 15000
    #employee_2 = employee_model.objects.filter(ename__endswith='is')#to get the employee records having ename field ends with the specified with case-sensitive
    #employee = employee_1.union(employee_2)
    #employee_1 = employee_model.objects.filter(esal__lt=15000)#to get the employee records having esal field lesser than 15000
    #manager_1 = manager_model.objects.filter(ename__endswith='on-Mngr')#to get the manager records having ename field ends with the specified with case-sensitive
    #employee = employee_1.union(manager_1)

    # TO SELECT ONLY SPECIFIC COLUMN IN A QUERY SET

    #employee = employee_model.objects.all().values('ename','esal')#to get the only the ename and esal column from employee records having esal field lesser than 15000 (using vakues())

    #AGGREGATE FUNCTIONS

    #avg=employee_model.objects.all().aggregate(Avg('esal'))
    #max=employee_model.objects.all().aggregate(Max('esal'))
    #min=employee_model.objects.all().aggregate(Min('esal'))
    #sum=employee_model.objects.all().aggregate(Sum('esal'))
    #count=employee_model.objects.all().aggregate(Count('esal'))
    #my_dict={'avg':avg,'max':max,'min':min,'sum':sum,'count':count}
    #return render(request,'firstApp/aggregate_display.html',context=my_dict)

    #TO PERFORM CRUD OPERATIONS

    #Create

    #e = employee_model(eno=2222,ename='mohamed thoufeeq',esal=12222,eadd='no:07 ekkambaram street, gokulam colony extention karanaipuducherry -603202')
    #e.save()
    #e = employee_model.objects.create(eno=2223,ename='mohammed hissam',esal=13333,eadd='rayapettai')
    #e.save()
    #employee_model.objects.bulk_create([employee_model(eno=2224,ename='magesh',esal=14444,eadd='thirunalvelli'),employee_model(eno=2225,ename='faraz ahamed',esal=15555,eadd='poondhamalle'),employee_model(eno=2226,ename='irfan ahamed',esal=16666,eadd='azathnagar')])
    #employee=employee_model.objects.all()

    #Delete

    #e = employee_model.objects.filter(eno__exact=9043)#to delete one or multiple record record
    #e.delete()
    #e = employee_model.objects.filter(esal__gte=15000)#to delete one or multiple record
    #print(e.count())
    #e.delete()
    #employee=employee_model.objects.all().delete()#to delete all records

    #Update

    #e=employee_model.objects.get(eno=5160)
    #print(e.ename)
    #e.ename='B.MOHAMED THOUFEEQ'
    #e.save()
    #employee=employee_model.objects.all()

    #SORTING RECORDS

    #employee=employee_model.objects.all().order_by('eno')#to order all records in ascending order (default) based on eno field of employee_model
    #employee=employee_model.objects.all().order_by('-eno')#to order all records in descending order (use '-' before the field) based on eno field of employee_model
    #employee=employee_model.objects.all().order_by('-esal')[0:3]#to get the top 3 highest paid employee
    #employee=employee_model.objects.all().order_by('ename')#to order all records in alphabatical order (default) based on ename field of employee_model
    #employee=employee_model.objects.all().order_by('-ename')#to order all records in reversed alphabatical order (use '-' before the field) based on ename field of employee_model
    my_dict={'employee':employee}
    return render(request,'firstApp/display.html',context=my_dict)
