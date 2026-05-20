from django.shortcuts import render 
from django.http import HttpResponse  # Ensure HttpResponse is imported 
from pdf_file.models import course1  # Assuming the model is 'Course' 
import csv 
from reportlab.lib.pagesizes import A4  
from reportlab.platypus import SimpleDocTemplate, Table  

# View to display the course list 
def courselist2(request): 
    courses = course1.objects.all() 
    return render(request, 'course_list.html', {'course_list1': courses}) 
 
# CSV generation view 
def generateCSV(request):  
    courses = course1.objects.all()  
    resp = HttpResponse(content_type="text/csv")  
    resp['Content-Disposition'] = 'attachment; filename=course_data.csv'  
 
    # Create a CSV writer object 
    writer = csv.writer(resp)  
    writer.writerow(['Course Code', 'Course Name', 'Course Credits'])  # Header row 
 
    # Write each course's data row 
    for c in courses:  
        writer.writerow([c.coursecode, c.coursename, c.credits])  
 
    return resp  
 
# PDF generation view 
def generatePDF(request):  
    courses = course1.objects.all()  
    resp = HttpResponse(content_type="application/pdf")  # Updated content type to application/pdf 
    resp['Content-Disposition'] = 'attachment; filename=course_data.pdf'  
 
    # Create the PDF document 
    pdf = SimpleDocTemplate(resp, pagesize=A4)  
    table_data = [['Course Code', 'Course Name', 'Course Credits']]  # Header row 
 
    # Add rows for each course 
    for c in courses:  
        table_data.append([c.coursecode, c.coursename, c.credits])  
 
    # Create the table and build the PDF 
    table = Table(table_data)  
    pdf.build([table])  
 
    return resp 
