from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from datetime import date,datetime
def home(request):
    return render(request,'front/top.html')


def Front_add_student(request,cor,bat,enquiry_id):
    form = Student_form()
    courseid = False
    data=False
    batch_data =False
    all_course = Master_course_data.objects.all()
    ins_list = []
    fee_type =[]
    admission_date = date.today()
    format_date = datetime.strptime(str(admission_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    enquiry_data = False


    if cor != "0" and bat == "0":

        courseid = Master_course_data.objects.filter(id = cor).first()

    if cor !="0" and bat != "0":
        if enquiry_id != "0":
            enquiry_data = Front_enquiry_data.objects.filter(id=enquiry_id).first()
            enquiry_data.status = 'close'
            enquiry_data.save()

        c = Master_course_data.objects.filter(id=cor).first()
        batch_data = Master_batch_data.objects.filter(id = bat).first()
        data = Master_fee_packege_data.objects.filter(course=c).first()
        number_of_student = c.front_student_data_set.count()
        date_list = list(format_date)
        fyear = date_list[8:]
        year = ''.join(fyear)

        if number_of_student == 0:
            roll_number = "TSP" + year + c.short_name + batch_data.batch_shot_name + '001'
            print(roll_number)

        else:
            num = number_of_student + 1
            if num<=9:
                roll_number = "TSP" + year + c.short_name + batch_data.batch_shot_name +"00" + str(num)
            if num > 9 and num < 100:
                roll_number = "TSP" + year + c.short_name + batch_data.batch_shot_name + "0" + str(num)
            if num > 99:
                roll_number = "TSP" + year + c.short_name + batch_data.batch_shot_name + str(num)

        if data:
            for i in data.master_make_installment_data_set.all():
                ins_list.append(int(i.percentage))

            for i in data.master_fee_type_packege_data_set.all():
                fee_type.append(int(i.fee))

            if request.method == "POST":

                form = Student_form(request.POST,request.FILES)

                if form.is_valid():

                    instance = form.save()
                    instance.course = c
                    instance.Batch = batch_data
                    instance.addmission_date = format_date
                    instance.total_fee_pay = '0'
                    instance.fee_after_pay = instance.total_fee
                    instance.Roll_number = roll_number
                    instance.save()

                    for f in data.master_fee_type_packege_data_set.all():
                        nam = 'feeType' + str(f.id)
                        student_fee = request.POST[nam]
                        student_data = Front_student_data.objects.filter(id = instance.id).first()


                        Front_student_fee_type_data.objects.create(student = student_data,name = f.fee_type,fee =student_fee )

                    for inst in data.master_make_installment_data_set.all():
                        nam2 = 'amount' + str(inst.id)

                        ins_amount = request.POST[nam2]
                        student_data = Front_student_data.objects.filter(id=instance.id).first()

                        Front_student_fee_installment_data.objects.create(student=student_data, installment=inst.name, amount=ins_amount
                                                                          ,pay_fee = '0',remaining_fee = ins_amount)

                    return redirect("Frontdesk:front_all_student")


    return render(request,'front/front_add_student.html',{"form":form,"courseid":courseid,"all_course":all_course,
                                                          "data":data,"ins_list":ins_list,"fee_type":fee_type
                                                          ,"batch_data":batch_data,"admission_date":format_date,
                                                          "enquiry_data":enquiry_data,"eid":enquiry_id})


def Front_view_edit_student(request,option,sid):
    student_data = Front_student_data.objects.filter(id = sid).first()
    couresid = student_data.course.id
    fee_packege = Master_fee_packege_data.objects.filter(course = couresid).first()
    num = 0
    for i in student_data.front_student_fee_type_data_set.all():
        num = num + int(i.fee)

    if option == "View":
        return render(request,'front/front_student_details.html',{"student_data":student_data,"fee_packege":fee_packege,"Total":num})


def Front_group_addmission(request,cor,bat,grp,enquiry_id):
    form = Student_form()

    courseid = False
    batchid = False
    groupid = False
    data = False
    grp_discount = False
    ins_list = []
    fee_type = []
    all_course = Master_course_data.objects.all()
    admission_date = date.today()
    format_date = datetime.strptime(str(admission_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    enquiry_data = False

    if cor != '0' and bat == '0' and grp == '0':
        courseid = Master_course_data.objects.filter(id = cor).first()


    if cor != '0' and bat != '0' and grp == '0':
        courseid = Master_course_data.objects.filter(id=cor).first()
        batchid =  Master_batch_data.objects.filter(id = bat).first()

    if cor != '0' and bat != '0' and grp != '0':
        if enquiry_id != "0":
            enquiry_data = Front_enquiry_data.objects.filter(id=enquiry_id).first()
            enquiry_data.status = 'close'
            enquiry_data.save()

        courseid = Master_course_data.objects.filter(id=cor).first()
        batchid = Master_batch_data.objects.filter(id=bat).first()
        groupid = Front_create_group_data.objects.filter(id=grp).first()
        data = Master_fee_packege_data.objects.get(course=courseid)

        a = groupid.min_range.split()
        min_student = int(a[2])
        number_of_student = groupid.front_student_data_set.count()
        if number_of_student == min_student:
            return render(request,'front/front_out_of_group_range.html',{"min_student":min_student,"group_data":groupid,
                                                                         "cor":cor,"bat":bat})

        for i in data.master_make_installment_data_set.all():
            ins_list.append(int(i.percentage))

        for i in data.master_fee_type_packege_data_set.all():
            fee_type.append(int(i.fee))

        if groupid.min_range == "2 to 5 student":
            grp_discount = data.discount_group_2_5

        elif groupid.min_range == "6 to 10 student":
            grp_discount = data.discount_group_6_11

        elif groupid.min_range == "11 to 20 student":
            grp_discount = data.discount_group_11_20

        elif groupid.min_range == "more than 20 student":
            grp_discount = data.discount_group_more_20

        else:
            pass
        if request.method == "POST":
            form = Student_form(request.POST,request.FILES)

            if form.is_valid():

                instance = form.save()
                instance.course = courseid
                instance.Batch = batchid
                instance.group = groupid


                instance.save()
                return redirect("Frontdesk:front_group_addmission",cor,bat,grp)

    return render(request, 'front/front_group_addmission.html',{"courseid":courseid,"all_course":all_course
                                                                ,"batchid":batchid,"groupid":groupid,"form":form,"data":data
                                                               ,"grp_discount":grp_discount,"ins_list":ins_list,"fee_type":fee_type
                                                                ,"admission_date":format_date,"enquiry_data":enquiry_data,"eid":enquiry_id})

def Front_create_group(request,cor):
    all_course = Master_course_data.objects.all()
    courseid = False
    if cor != "0":
        courseid = Master_course_data.objects.filter(id = cor).first()
        if request.method == "POST":
            d = request.POST
            batch_id = d['batch']
            batch = Master_batch_data.objects.filter(id = batch_id).first()
            name = d['group_name']
            min_range = d['min_range']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')

            Front_create_group_data.objects.create(course = courseid,batch=batch,group_name = name,min_range=min_range
                                                   ,created_date = format_date)

            return redirect('Frontdesk:front_group_addmission','0','0','0')


    return render(request,'front/front_create_group.html',{"courseid":courseid,"all_course":all_course})

def Front_all_group(request):
    all_group = Front_create_group_data.objects.all()
    return render(request,'front/front_group_list.html',{"all_group":all_group})

def Front_edit_group(request,gid):
    group_data = Front_create_group_data.objects.filter(id=gid).first()

    all_course = Master_course_data.objects.all()
    cid = group_data.course.id
    courseid = Master_course_data.objects.filter(id = cid).first()
    if request.method == "POST":
        c = request.POST['course']
        b = request.POST['batch']
        mr = request.POST['min_range']
        name = request.POST['group_name']
        course = Master_course_data.objects.filter(id = c).first()
        batch = Master_batch_data.objects.filter(id = b).first()
        group_data.group_name = name
        group_data.course = course
        group_data.batch = batch
        group_data.min_range = mr
        group_data.save()
        return redirect('Frontdesk:front_group_addmission','0','0','0')



    return render(request,'front/front_edit_group.html',{"group_data":group_data,
                                                             "all_course":all_course,"courseid":courseid})

def Front_all_student(request):
    all_student = Front_student_data.objects.all()
    all_group = Front_create_group_data.objects.all()

    return render(request,'front/all_student.html',{"all_student":all_student,"all_group":all_group})

def Front_enquiry(request):
    form = Enquiry_form()
    open_enquiry = Front_enquiry_data.objects.filter(status = 'open')
    close_enquiry = Front_enquiry_data.objects.filter(status = 'close')
    today_date = date.today()
    format_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')

    if request.method == "POST":
        form = Enquiry_form(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.visited_date = format_date
            instance.status = 'open'
            instance.save()
            return redirect('Frontdesk:front_enquiry')
        else:
            form = Enquiry_form()

    return render(request,'front/front_enquiry.html',{"form":form,"open_enquiry":open_enquiry
                                                      ,"visited_date":format_date,"close_enquiry":close_enquiry})

def Front_close_enquiry_or_update_followup(request,option,eid):
    data = Front_enquiry_data.objects.filter(id=eid).first()
    if option == "Close":
        data.status = 'close'
        data.save()
        return redirect('Frontdesk:front_enquiry')
    if option == "Update":
        if request.method == "POST":
            d = request.POST
            fdate = d['fdate']
            ftime = d['ftime']
            remark = d['remark']
            data.follow_uo_time = ftime
            data.follow_uo_date = fdate
            data.remark = remark
            data.save()
            return redirect('Frontdesk:front_enquiry')
        return render(request,'front/front_update_folloup.html',{"data":data})


def Front_view_enquiry(request,eid):
    data = Front_enquiry_data.objects.get(id = eid)
    return render(request,'front/front_view_enquiry.html',{"data":data})

def Front_enquiry_followup_reminder(request):
    open_enquiry = Front_enquiry_data.objects.filter(status = 'open')
    today_date = date.today()
    format_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    date_split = format_date.split('/')
    date_reverse = date_split[3::-1]
    number1 = int(''.join(date_reverse))
    li = []
    a = 0
    for fdate in open_enquiry:
        follow_date = fdate.follow_up_date
        follow_date_split = follow_date.split('/')

        follow_date_reverse = follow_date_split[3::-1]
        number2 = int(''.join(follow_date_reverse))
        if a == 5:
            break
        if number2 > number1:
            li.append(fdate)
            a = a+1

    return render(request,'front/front_followup_reminder.html',{"open_enquiry":open_enquiry,"latest_followup_date":li})

############## pay fee ############

def Front_student_collect_fee(request,cor,bat):
    all_course = Master_course_data.objects.all()
    payment_mode = Master_paymentmode_data.objects.all()
    student_data = False
    batch = False
    course = False
    today_date = date.today()
    payment_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
    li = []
    for mode in payment_mode:
        li.append(mode.name)
    if cor != '0' and bat == '0':
        course = Master_course_data.objects.filter(id = cor).first()
    if cor != '0' and bat != '0':
        batch_data = Master_batch_data.objects.filter(id = bat).first()
        student_data = batch_data.front_student_data_set.all()
        batch = batch_data


    return render(request,'front/front_collect_fee.html',{"student_data":student_data,
                                                          "all_course":all_course,"course":course,"batch":batch
                                                          ,"payment_date":payment_date,"payment_mode":payment_mode,"payment_name":li})

########## Student Attendence #############

def Front_student_attendence(request,cor,bat):
    all_course = Master_course_data.objects.all()
    course = False
    batch = False
    student_attendence = False
    students = False
    if cor!= '0':
        course = Master_course_data.objects.filter(id = cor).first()
    if cor!= '0' and bat != '0':
        batch = Master_batch_data.objects.filter(id = bat).first()
        students = batch.front_student_data_set.all()


    return render(request,'front/front_all_student_attendence.html',{"all_course":all_course,"course":course,"batch":batch,
                                                                     "student_attendence":student_attendence,"students":students})
























