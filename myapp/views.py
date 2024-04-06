from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .models import Teacher,Student

def index(request):
    return render(request,'myapp/index.html')

def studentsignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        courses = request.POST.get('courses')
        subjects = request.POST.get('subjects')
        tution_location = request.POST.get('tution_location')
        preferred_timing = request.POST.get('preferred_timing')
        preferred_tutor = request.POST.get('preferred_tutor')
        fee_offered = request.POST.get('fee_offered')
        tution_type = request.POST.get('tution_type')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        locality = request.POST.get('locality')
        is_at_student_home = request.POST.get('IsAtStudentHome', False)
        is_at_tutor_home = request.POST.get('IsAtTutorHome', False)
        is_at_institute = request.POST.get('IsAtInstitute', False)
        is_online_tuition = request.POST.get('IsOnlineTuition', False)
        tution_desc = request.POST.get('tution_desc')
        
        # Concatenating the checked values into a single string
        tution_location = ''
        if is_at_student_home:
            tution_location += 'At My Home, '
        if is_at_tutor_home:
            tution_location += 'At Tutor\'s Home, '
        if is_at_institute:
            tution_location += 'At Institute, '
        if is_online_tuition:
            tution_location += 'Online Tuition'
        # Creating a new Student instance
        # Student.objects.create(
        #     user=request.user,
        #     full_name=full_name,
        #     phone=phone,
        #     courses=courses,
        #     subjects=subjects,
        #     tution_location=tution_location,
        #     preferred_timing=preferred_timing,
        #     preferred_tutor=preferred_tutor,
        #     fee_offered=fee_offered,
        #     tution_type=tution_type,
        #     pincode=pincode,
        #     city=city,
        #     locality=locality
        # )
        
        print(tution_location)
        print('this is post request ')
        print("Name:", full_name)
        print("Email:", email)
        print("Phone:", phone)
        print("Password:", password)
        print("Confirm Password:", cpassword)
        print("Subject:", subjects)
        print("Class:", courses)
        print("Address:", city)
        print("Pincode:", pincode)
        # print(f"{name} {email}{password}")
        user = User.objects.create_user(username=email, email=email, password=password)
        student=Student.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            courses=courses,
            subjects=subjects,
            tution_location=tution_location,
            preferred_timing=preferred_timing,
            preferred_tutor=preferred_tutor,
            fee_offered=fee_offered,
            tution_type=tution_type,
            pincode=pincode,
            city=city,
            locality=locality,
            tution_desc=tution_desc
        )
        student.save()
        
    
        return redirect('index')
    return render (request,'myapp/studentsignup.html')

def tutorsignup(request):
    if request.method == 'POST':
        print("this is post request")
        # for user objects 
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        phone=request.POST.get('phone')
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        city = request.POST.get('city')
        locality = request.POST.get('locality')
        landmark = request.POST.get('landmark')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        category = request.POST.get('category')
        courses = request.POST.get('courses')
        subjects = request.POST.get('subjects')
        qualification = request.POST.get('qualification')
        college = request.POST.get('college')
        university = request.POST.get('university')
        experience = request.POST.get('experience')
        hourly_price = request.POST.get('hourly_price')
        preferred_timing = request.POST.get('preferred_timing')
        about_me = request.POST.get('about_me')
         
        print(full_name)
        print(email)
        print(password)
        print(hourly_price)
        print(pincode)
        print(qualification)

        # You can create an instance of your model and save the data
        # Example:
        user=User.objects.create_user(username=email,password=password)
        user.save()
        print(user)
        # user=user.username
        print(user)
        Teacher.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            gender=gender,
            age=age,
            city=city,
            locality=locality,
            landmark=landmark,
            address=address,
            pincode=pincode,
            category=category,
            courses=courses,
            subjects=subjects,
            qualification=qualification,
            college=college,
            university=university,
            experience=experience,
            hourly_price=hourly_price,
            preferred_timing=preferred_timing,
            about_me=about_me
        ).save()
        # You can also handle the image upload if needed
        # Example:
        # profile_img = request.FILES.get('profile_img')
        # if profile_img:
        #     YourModel.objects.profile_img = profile_img
        #     YourModel.save()

        return redirect('index')
    return render (request,'myapp/tutorsignup.html')

def signin(request):
    if request.method == 'POST':
        # Extract username and password from the form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Email:", username)
        # print("Phone:", phone)
        print("Password:", password)
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log the user in
            login(request, user)
            # Redirect to a success page or any desired page
            return redirect('index')  # Replace 'success_page_url' with the desired URL
        else:
            # If authentication fails, render the login form with an error message
            error_message = "Invalid username or password."
            return render(request, 'myapp/signin.html', {'error_message': error_message})
       
    return render (request,'myapp/signin.html')

def signout(request):
    
    logout(request)
    return redirect ('index')

def search(request):
    if request.method == 'POST':
        print("this is post request")
        citySearch = request.POST.get('city')
        searchTypeDropdown = request.POST.get('searchTypeDropdown')
        SearchText = request.POST.get('SearchText')
        Subject = request.POST.get('subject')
        courses = request.POST.get('courses')
        pincode = request.POST.get('pincode')
        data = searchTypeDropdown
        print(data)
        if data == "tutors":
            request.session['search_type'] = data
            print("tutor")
            # if citySearch is not None and SearchText is not None and Subject is not None and courses is not None and pincode is not None:
            #     teacher = Teacher.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText, subjects__icontains=Subject, courses__icontains=courses, pincode_icontains=pincode)
            #     teacher = Teacher.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText, subjects__icontains=Subject, courses__icontains=courses, pincode_icontains=pincode)
            # else:
            teacher = Teacher.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText, subjects__icontains = Subject , courses__icontains = courses, pincode_icontains = pincode )
            # teacher = Teacher.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText, subjects__icontains=Subject, courses__icontains=courses, pincode_icontains=pincode)
            print(teacher)
            return render(request, "myapp/tutorsearch.html", {"teacher": teacher})
        elif data == "tuitions":
            print("student")
            request.session['search_type'] = data
            # if citySearch is not None and SearchText is not None and Subject is not None and courses is not None and pincode is not None:
            #     student = Student.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText, subjects__icontains=Subject, courses__icontains=courses, pincode_icontains=pincode)
            # else:
            student = Student.objects.filter(city__icontains=citySearch, full_name__icontains=SearchText )

            print(student)
            return render(request, "myapp/studentsearch.html", {"student": student})
        
    data = request.session.get('search_type', "tutor")
    if data == "tutor":
        print("tutor")
        teacher = Teacher.objects.all()
        return render(request, "myapp/tutorsearch.html", {"teacher": teacher})
    elif data == "student":
        print("student")
        student = Student.objects.all()
        return render(request, "myapp/studentsearch.html", {"student": student})

    student = Student.objects.all()
    print(student)
    return render(request, "myapp/studentsearch.html", {"student": student})

def studetails (request,pk):
    print(pk)
    student =Student.objects.filter(id=pk).first()
    return render (request,'myapp/studetails.html',{"student":student})

def tutordetails (request,pk):
    print(pk)
    teacher = Teacher.objects.filter(id=pk).first()
    return render (request,'myapp/tutordetails.html',{"teacher":teacher})