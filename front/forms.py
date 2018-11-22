
from .models import *
from django import forms
from datetime import date,datetime
class Student_form(forms.ModelForm):
    class Meta:
        model = Front_student_data

        exclude = ('course', 'Batch','addmission_date','group','fee_after_pay','total_fee_pay'
                   ,'Roll_number')
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name',
                                           'class': 'form-control',
                                           "required":''}),

            "image": forms.FileInput(attrs={'class': 'form-control',
                                           "required": '',
                                            "onchange":"readURL(this);"}),
            "dob": forms.TextInput(attrs={'placeholder': 'Date of Birth',
                                           'class': 'form-control'
                                          ,"required":''
                                          }),
            "address": forms.TextInput(attrs={'placeholder': 'Address',
                                          'class': 'form-control'
                                              ,"required":''}),
            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile Number',
                                          'class': 'form-control',
                                             "required": ''}),
            "email": forms.TextInput(attrs={'placeholder': 'Email Address',
                                          'class': 'form-control',
                                            "required": ''}),
            "college": forms.TextInput(attrs={'placeholder': 'College/School',
                                          'class': 'form-control',
                                              "required": ''}),
            "graduation": forms.TextInput(attrs={'placeholder': 'Graduation/Standard',
                                          'class': 'form-control',
                                                 "required": ''  }),

            "gender": forms.Select(attrs={'name': 'gender',
                                     'class': 'form-control show-tick',
                                          "required": ''
                                     }),
            "stream": forms.TextInput(attrs={'placeholder': 'Stream/Subject',
                                                 'class': 'form-control',
                                             "required": ''
                                                 }),
            "Father_name": forms.TextInput(attrs={'placeholder': 'Father\'s name',
                                             'class': 'form-control',
                                                  "required": ''
                                             }),
            "father_mob": forms.TextInput(attrs={'placeholder': 'Father\'s Contact No.',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "father_add": forms.TextInput(attrs={'placeholder': 'Father\'s Address',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "Occupation": forms.TextInput(attrs={'placeholder': 'Father\'s Occupation',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "discount": forms.TextInput(attrs={'placeholder': 'Discount',
                                                 'class': 'form-control',

                                                 "value":"0",
                                                 "id":"discount_id",
                                                "onkeyup":"myFunction3();"

                                                 }),
            "total_fee": forms.TextInput(attrs={'placeholder': 'Total Fee',
                                               'class': 'form-control', "id":'total_fee_id',
                                                "readonly":""
                                               }),
        }



class Enquiry_form(forms.ModelForm):
    class Meta:
        model = Front_enquiry_data
        today_date = date.today()
        format_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
        exclude = ('visited_date','status')
        widgets = {
            "course": forms.Select(attrs={'class': 'form-control show-tick', "required": '1',
                                          }),
            "student_name": forms.TextInput(attrs={'placeholder': 'Name',
                                           'class': 'form-control',"required":'1'}),
            "father_name": forms.TextInput(attrs={'placeholder': 'Fathers\'name',
                                                   'class': 'form-control', "required": '1'}),

            "address": forms.TextInput(attrs={'placeholder': 'Address',
                                              'class': 'form-control',"required":'1'}),

            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile Number',
                                             'class': 'form-control',"required":'1'}),

            "email": forms.EmailInput(attrs={'placeholder': 'Email Address',
                                            'class': 'form-control',"required":'1'}),

            "college": forms.TextInput(attrs={'placeholder': 'College/School',
                                              'class': 'form-control',"required":'1'}),

            "graduation": forms.TextInput(attrs={'placeholder': 'Graduation/Standard',
                                                 'class': 'form-control',"required":'1'
                                                 }),



            "remark": forms.TextInput(attrs={'placeholder': 'Remark',
                                             'class': 'form-control',"required":'1'
                                             }),

            "follow_up_date": forms.DateInput(attrs={'placeholder': 'Follow Up Date',
                                                  'class': 'form-control',"required":'1',
                                                     'name':'follow_up_date',"maxlength":'10',
                                                     "size":'15'
                                                  }),
            "follow_up_time": forms.TextInput(attrs={'placeholder': 'Follow Up Time',
                                                     'class': 'form-control', "required": '1'
                                                     }),

    }



