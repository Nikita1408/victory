from django.db import models
from Institute.models import *
from django.forms import ModelForm\

COLOR_CHOICES = (
    ('','Gender'),
    ('male','Male'),
    ('female', 'Female'),

)


class Front_create_group_data(models.Model):
    course = models.ForeignKey(Master_course_data,models.CASCADE,null=True)
    batch = models.ForeignKey(Master_batch_data, models.CASCADE, null=True)
    group_name = models.CharField(max_length=100, null=True)
    min_range = models.CharField(max_length=100,null=True)
    created_date = models.CharField(max_length=100,null=True)

    def __str__(self):
       return self.course.name + '--' + self.batch.name +  '--' + self.group_name



class Front_student_data(models.Model):

    group = models.ForeignKey(Front_create_group_data,models.CASCADE,null= True,blank=True)


    ##### Course Details ########
    course = models.ForeignKey(Master_course_data,models.CASCADE, null=True,
                              default='',blank=True )
    Batch = models.ForeignKey(Master_batch_data,models.CASCADE, null=True,default='',blank=True)
    Roll_number = models.CharField(max_length=100,null=True,blank=True)

    ##### Basic Details #######
    image = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    dob = models.CharField(max_length=20, null=True,blank=True)
    address = models.TextField(max_length=500, null=True,blank=True)
    mobile = models.CharField(max_length=13, null=True,blank=True)
    email = models.CharField(max_length=100, null=True,blank=True)
    college = models.CharField(max_length=100, null=True,blank=True)
    graduation = models.CharField(max_length=100, null=True,blank=True)
    stream = models.CharField(max_length=100, null=True,blank=True)
    gender = models.CharField(max_length=10,choices=COLOR_CHOICES,default='Gender')
    #### Parents Details #########
    Father_name = models.CharField(max_length=100, null=True,blank=True)
    father_mob = models.CharField(max_length=13, null=True,blank=True)
    Occupation = models.CharField(max_length=100, null=True,blank=True)
    father_add = models.CharField(max_length=200, null=True,blank=True)
    ##### Fee Details #######
    discount = models.CharField(max_length=100, null=True,blank=True)
    total_fee = models.CharField(max_length=100, null=True,blank=True)
    addmission_date = models.CharField(max_length=100, null=True,blank=True)
    total_fee_pay = models.CharField(max_length=100, null=True, blank=True)
    fee_after_pay = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name + '  course  ' + self.course.name + ' batchName ' + self.Batch.name

class Front_student_fee_type_data(models.Model):
    student = models.ForeignKey(Front_student_data,models.CASCADE,null=True)
    name =  models.CharField(max_length=100,null=True)
    fee =  models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.student.name + '--' + self.name + '--' + self.fee

class Front_student_fee_installment_data(models.Model):
    student = models.ForeignKey(Front_student_data,models.CASCADE,null=True)
    installment = models.CharField(max_length=100,null=True)
    amount = models.CharField(max_length=100,null=True)
    pay_fee = models.CharField(max_length=100,null=True)
    remaining_fee = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.student.name + ' ' + self.installment + ' amount ' + self.amount

class Front_student_pay_fee(models.Model):
    student = models.ForeignKey(Front_student_data, models.CASCADE, null=True)
    payment_mode = models.CharField(max_length=100,null=True)
    amount = models.CharField(max_length=100,null=True)
    payment_date = models.CharField(max_length=100,null=True)






class Front_enquiry_data(models.Model):
    course = models.ForeignKey(Master_course_data,models.CASCADE,null=True ,default='')
    student_name = models.CharField(max_length=100,null=True)
    father_name = models.CharField(max_length=100,null=True)
    college = models.CharField(max_length=100,null=True)
    graduation = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=13,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    follow_up_date = models.CharField(max_length=10,null=True)
    follow_up_time = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=500,null=True)
    visited_date = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student_name + ' -- ' + self.course.name

##########Attendence #############
class Front_student_attendence_data(models.Model):
    student = models.ForeignKey(Front_student_data,models.CASCADE,null=True)
    atted_date = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student.name + '  ' + self.atted_date












