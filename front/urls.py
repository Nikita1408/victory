from django.conf.urls import url,include
from django.contrib import admin
from Frontdesk.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Frontdesk"
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name = 'home'),
    url(r'^all_students/$', Front_all_student,name = 'front_all_student'),
    url(r'^student/(?P<option>[\w-]+)/(?P<sid>[0-9]+)/$', Front_view_edit_student,name = 'front_VED_student'),
    url(r'^all_groups/$', Front_all_group,name = 'front_all_group'),
    url(r'^single-student-addmission/(?P<cor>[\w-]+)/(?P<bat>[\w-]+)/(?P<enquiry_id>[\w-]+)/$', Front_add_student,name = 'front_add_student'),
    url(r'^create-group/(?P<cor>[\w-]+)/$', Front_create_group, name='front_create_group'),
    url(r'^group/(?P<gid>[0-9]+)/$', Front_edit_group, name='front_edit_group'),
    url(r'^group-student-addmission/(?P<cor>[\w-]+)/(?P<bat>[\w-]+)/(?P<grp>[\w-]+)/(?P<enquiry_id>[\w-]+)/$', Front_group_addmission, name='front_group_addmission'),
    ######Enquiry#######
    url(r'^enquiry_list/$', Front_enquiry, name='front_enquiry'),
    url(r'^enquiry/(?P<option>[\w-]+)/(?P<eid>[0-9]+)/$', Front_close_enquiry_or_update_followup, name='front_close_or_update'),
    url(r'^details_enquiry/(?P<eid>[0-9]+)/$', Front_view_enquiry, name='front_view_enquiry'),
    url(r'^enquiry_followup_Reminder/$', Front_enquiry_followup_reminder, name='front_enquiry_followup_reminder'),

######### Fee Pay ############
    url(r'^student_Fee_details/(?P<cor>[\w-]+)/(?P<bat>[\w-]+)/$', Front_student_collect_fee, name='front_fee_details'),

############Student Attendence ##############
    url(r'^students_attendence/(?P<cor>[\w-]+)/(?P<bat>[\w-]+)/$', Front_student_attendence, name='front_all_student_attendence'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


