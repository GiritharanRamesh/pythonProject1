from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Compensationinfo, Employee1, Contact1, Emergencycontact, Experience1, Jobinfo, Leaveinfo, Managementinfo, Nationalinfo, Organization1, Personalinfo, Qualification1, Skills1, Timesheetinfo, Bankdetails
from .serializers import EmployeeSerializer, CompensationInfoSerializer, ContactSerializer, EmergencySerializer, ExperienceSerializer, JobInfoSerializer, LeaveInfoSerializer, ManagementInfoSerializer, NationalInfoSerializer, OrganizationSerializer, PersonalInfoSerializer, QualificationSerializer, SkillsSerializer, TimeSheetSerializer, BankDetailsSerializer



# Employee Views.


@csrf_exempt
def employee_Api(request, id=0):
    if request.method == 'GET':
        Employees = Employee1.objects.filter(id)
        employee_table_serializer = EmployeeSerializer(Employees, many=True)
        return JsonResponse(employee_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Employee_data = JSONParser().parse(request)
        employee_table_serializer = EmployeeSerializer(data=Employee_data)
        if employee_table_serializer.is_valid():
            employee_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Employee_data = JSONParser().parse(request)
        Employee = Employee1.objects.get(empid=Employee_data['empid'])
        employee_table_serializer = EmployeeSerializer(Employee, data=Employee_data)
        if employee_table_serializer.is_valid():
            employee_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Employee = Employee1.objects.get(empid=id)
        Employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

# CompensationInfo Views.

@csrf_exempt
def compensationinfo_Api(request, id=0):
    if request.method == 'GET':
        CompensationInfo = Compensationinfo.objects.all()
        compensation_info_serializer = CompensationInfoSerializer(CompensationInfo, many=True)
        return JsonResponse(compensation_info_serializer.data, safe=False)
    elif request.method == 'POST':
        Compensationinfo_data = JSONParser().parse(request)
        compensation_info_serializer = CompensationInfoSerializer(data=Compensationinfo_data)
        if compensation_info_serializer.is_valid():
            compensation_info_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Compensationinfo_data = JSONParser().parse(request)
        CompensationInfo = Compensationinfo.objects.get(empid=Compensationinfo_data['empid'])
        compensation_info_serializer=CompensationInfoSerializer(CompensationInfo, data=Compensationinfo_data)
        if compensation_info_serializer.is_valid():
            compensation_info_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        CompensationInfo = Compensationinfo.objects.get(empid=id)
        CompensationInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)



# Contact views

@csrf_exempt
def contact_Api(request, id=0):
    if request.method == 'GET':
        Contact = Contact1.objects.all()
        contact_table_serializer = ContactSerializer(Contact, many=True)
        return JsonResponse(contact_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Contact_data = JSONParser().parse(request)
        contact_table_serializer = ContactSerializer(data=Contact_data)
        if contact_table_serializer.is_valid():
            contact_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Contact_data = JSONParser().parse(request)
        Contact = Contact1.objects.get(empid=Contact_data['empid'])
        contact_table_serializer=ContactSerializer(Contact, data=Contact_data)
        if contact_table_serializer.is_valid():
            contact_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Contact = Contact1.objects.get(empid=id)
        Contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)



# Emergency contact views.

@csrf_exempt
def emergency_Api(request, id=0):
    if request.method == 'GET':
        Emergency = Emergencycontact.objects.all()
        emergency_table_serializer = EmergencySerializer(Emergency, many=True)
        return JsonResponse(emergency_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Emergency_data = JSONParser().parse(request)
        emergency_table_serializer = EmergencySerializer(data=Emergency_data)
        if emergency_table_serializer.is_valid():
            emergency_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Emergency_data = JSONParser().parse(request)
        Emergency = Emergencycontact.objects.get(empid=Emergency_data['empid'])
        emergency_table_serializer=EmergencySerializer(Emergency, data=Emergency_data)
        if emergency_table_serializer.is_valid():
            emergency_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Emergency = Emergencycontact.objects.get(empid=id)
        Emergency.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)



# Experience Views.

@csrf_exempt
def experience_Api(request, id=0):
    if request.method == 'GET':
        Experience = Experience1.objects.all()
        experience_table_serializer = ExperienceSerializer(Experience, many=True)
        return JsonResponse(experience_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Experience_data = JSONParser().parse(request)
        experience_table_serializer = ExperienceSerializer(data=Experience_data)
        if experience_table_serializer.is_valid():
            experience_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Experience_data = JSONParser().parse(request)
        Experience = Experience1.objects.get(empid=Experience_data['empid'])
        experience_table_serializer=ExperienceSerializer(Experience, data=Experience_data)
        if experience_table_serializer.is_valid():
            experience_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Experience = Experience1.objects.get(empid=id)
        Experience.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)



# JobInfo Views.

@csrf_exempt
def jobinfo_Api(request, id=0):
    if request.method == 'GET':
        JobInfo = Jobinfo.objects.all()
        job_info_table_serializer = JobInfoSerializer(JobInfo, many=True)
        return JsonResponse(job_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Job_info_data = JSONParser().parse(request)
        job_info_table_serializer = JobInfoSerializer(data=Job_info_data)
        if job_info_table_serializer.is_valid():
            job_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Job_info_data = JSONParser().parse(request)
        JobInfo = Jobinfo.objects.get(empid=Job_info_data['empid'])
        job_info_table_serializer=JobInfoSerializer(JobInfo, data=Job_info_data)
        if job_info_table_serializer.is_valid():
            job_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        JobInfo = Jobinfo.objects.get(empid=id)
        JobInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)



# LeaveInfo Views.

@csrf_exempt
def leaveinfo_Api(request, id=0):
    if request.method == 'GET':
        LeaveInfo = Leaveinfo.objects.all()
        leave_info_table_serializer = LeaveInfoSerializer(LeaveInfo, many=True)
        return JsonResponse(leave_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Leave_info_data = JSONParser().parse(request)
        leave_info_table_serializer = LeaveInfoSerializer(data=Leave_info_data)
        if leave_info_table_serializer.is_valid():
            leave_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Leave_info_data = JSONParser().parse(request)
        LeaveInfo = Leaveinfo.objects.get(empid=Leave_info_data['empid'])
        leave_info_table_serializer=LeaveInfoSerializer(LeaveInfo, data=Leave_info_data)
        if leave_info_table_serializer.is_valid():
            leave_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        LeaveInfo = Leaveinfo.objects.get(empid=id)
        LeaveInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)


# ManagementInfo Views.

@csrf_exempt
def managementinfo_Api(request, id=0):
    if request.method == 'GET':
        ManagementInfo = Managementinfo.objects.all()
        management_info_table_serializer = ManagementInfoSerializer(ManagementInfo, many=True)
        return JsonResponse(management_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Management_info_data = JSONParser().parse(request)
        management_info_table_serializer = ManagementInfoSerializer(data=Management_info_data)
        if management_info_table_serializer.is_valid():
            management_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Management_info_data = JSONParser().parse(request)
        ManagementInfo = Managementinfo.objects.get(empid=Management_info_data['empid'])
        management_info_table_serializer=ManagementInfoSerializer(ManagementInfo, data=Management_info_data)
        if management_info_table_serializer.is_valid():
            management_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        ManagementInfo = Managementinfo.objects.get(empid=id)
        ManagementInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)


# NationalInfo Views.

@csrf_exempt
def nationalinfo_Api(request, id=0):
    if request.method == 'GET':
        NationalInfo = Nationalinfo.objects.all()
        national_info_table_serializer = NationalInfoSerializer(NationalInfo, many=True)
        return JsonResponse(national_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        National_info_data = JSONParser().parse(request)
        national_info_table_serializer = NationalInfoSerializer(data=National_info_data)
        if national_info_table_serializer.is_valid():
            national_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        National_info_data = JSONParser().parse(request)
        NationalInfo = Nationalinfo.objects.get(empid=National_info_data['empid'])
        national_info_table_serializer=NationalInfoSerializer(NationalInfo, data=National_info_data)
        if national_info_table_serializer.is_valid():
            national_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        NationalInfo = Nationalinfo.objects.get(empid=id)
        NationalInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)


# Organization Views.

@csrf_exempt
def organization_Api(request, id=0):
    if request.method == 'GET':
        Organization = Organization1.objects.all()
        organization_table_serializer = OrganizationSerializer(Organization, many=True)
        return JsonResponse(organization_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Organization_data = JSONParser().parse(request)
        organization_table_serializer = OrganizationSerializer(data=Organization_data)
        if organization_table_serializer.is_valid():
            organization_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Organization_data = JSONParser().parse(request)
        Organization = Organization1.objects.get(empid=Organization_data['empid'])
        organization_table_serializer = OrganizationSerializer(Organization, data=Organization_data)
        if organization_table_serializer.is_valid():
            organization_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Organization = Organization1.objects.get(empid=id)
        Organization.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)



# PersonalInfo Views.

@csrf_exempt
def personalinfo_Api(request, id=0):
    if request.method == 'GET':
        PersonalInfo = Personalinfo.objects.all()
        personal_info_table_serializer = PersonalInfoSerializer(PersonalInfo, many=True)
        return JsonResponse(personal_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Personal_Info_data = JSONParser().parse(request)
        personal_info_table_serializer = PersonalInfoSerializer(data=Personal_Info_data)
        if personal_info_table_serializer.is_valid():
            personal_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Personal_Info_data = JSONParser().parse(request)
        PersonalInfo = Personalinfo.objects.get(empid=Personal_Info_data['empid'])
        personal_info_table_serializer = PersonalInfoSerializer(PersonalInfo, data=Personal_Info_data)
        if personal_info_table_serializer.is_valid():
            personal_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        PersonalInfo = Personalinfo.objects.get(empid=id)
        PersonalInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)



# Qualification Views.

@csrf_exempt
def qualification_Api(request, id=0):
    if request.method == 'GET':
        Qualification = Qualification1.objects.all()
        qualification_table_serializer = QualificationSerializer(Qualification, many=True)
        return JsonResponse(qualification_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Qualification_data = JSONParser().parse(request)
        qualification_table_serializer = QualificationSerializer(data=Qualification_data)
        if qualification_table_serializer.is_valid():
            qualification_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Qualification_data = JSONParser().parse(request)
        Qualification = Qualification1.objects.get(empid=Qualification_data['empid'])
        qualification_table_serializer = QualificationSerializer(Qualification, data=Qualification_data)
        if qualification_table_serializer.is_valid():
            qualification_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Qualification = Qualification1.objects.get(empid=id)
        Qualification.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)



# Skills Views.

@csrf_exempt
def skills_Api(request, id=0):
    if request.method == 'GET':
        Skills = Skills1.objects.all()
        skills_table_serializer = SkillsSerializer(Skills, many=True)
        return JsonResponse(skills_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Skills_data = JSONParser().parse(request)
        skills_table_serializer = SkillsSerializer(data=Skills_data)
        if skills_table_serializer.is_valid():
            skills_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Skills_data = JSONParser().parse(request)
        Skills = Skills1.objects.get(empid=Skills_data['empid'])
        skills_table_serializer = SkillsSerializer(Skills, data=Skills_data)
        if skills_table_serializer.is_valid():
            skills_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Skills = Skills1.objects.get(empid=id)
        Skills.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)



# TimeSheetInfo Views.

@csrf_exempt
def timesheet_Api(request, id=0):
    if request.method == 'GET':
        Time_Sheet = Timesheetinfo.objects.all()
        time_sheet_table_serializer = TimeSheetSerializer(Time_Sheet, many=True)
        return JsonResponse(time_sheet_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Time_Sheet_data = JSONParser().parse(request)
        time_sheet_table_serializer = TimeSheetSerializer(data=Time_Sheet_data)
        if time_sheet_table_serializer.is_valid():
            time_sheet_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Time_Sheet_data = JSONParser().parse(request)
        Time_Sheet = Timesheetinfo.objects.get(empid=Time_Sheet_data['empid'])
        time_sheet_table_serializer = TimeSheetSerializer(Time_Sheet, data=Time_Sheet_data)
        if time_sheet_table_serializer.is_valid():
            time_sheet_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Time_Sheet = Timesheetinfo.objects.get(empid=id)
        Time_Sheet.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


# BankDetails Views.

@csrf_exempt
def bankdetails_Api(request, id=0):
    if request.method == 'GET':
        BankDetails = Bankdetails.objects.all()
        bank_details_table_serializer = BankDetailsSerializer(BankDetails, many=True)
        return JsonResponse(bank_details_table_serializer.data, safe=False)
    elif request.method == 'POST':
        BankDetails_data = JSONParser().parse(request)
        bank_details_table_serializer = BankDetailsSerializer(data=BankDetails_data)
        if bank_details_table_serializer.is_valid():
            bank_details_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        BankDetails_data = JSONParser().parse(request)
        BankDetails = Bankdetails.objects.get(empid=BankDetails_data['empid'])
        bank_details_table_serializer=BankDetailsSerializer(BankDetails, data=BankDetails_data)
        if bank_details_table_serializer.is_valid():
            bank_details_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        BankDetails = Bankdetails.objects.get(empid=id)
        BankDetails.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)


