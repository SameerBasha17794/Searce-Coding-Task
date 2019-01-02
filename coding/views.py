from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import zira
from .forms import ZiraForm
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import AddZiraSerializer,SearchSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def home(request):
	return render(request,'home.html',{})

@login_required
def addzira(request):
	if request.method=='POST':
		form = ZiraForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.uploaded_by = request.user
			a.save()	
			messages.success(request,'Successfully Added')
		else:
			messages.error(request,'Something Went Wrong Please Try again !!!')	

	form = ZiraForm()
	return render(request,'addzira.html',{'form':form})

@login_required
def viewzira(request):
	a = zira.objects.all()
	return render(request,'viewzira.html',{'a':a})	

@login_required
def editzira(request,pk):
	z = zira.objects.get(pk=pk)
	zira_form = ZiraForm(instance = z)
	if request.method=='POST':
		form = ZiraForm(request.POST, instance = z)
		if form.is_valid():
			form.save()	
			messages.success(request,'Zira Updated')
			return redirect('viewzira')

	form = ZiraForm()
	return render(request,'ziraedit.html',{'form':zira_form})

@login_required
def deletezira(request,pk):
	a = zira.objects.get(pk=pk)
	a.delete()
	messages.success(request,'Successfully Deleted')
	return redirect('viewzira')

class addziraapi(APIView):
	serializer_class = AddZiraSerializer

	def post(self,request,*args,**kwargs):
		data = request.data
		ticket_num = data['ticket_num']
		issue_description = data['issue_description']
		uploaded_by = request.user
		if ticket_num and zira.objects.filter(ticket_num=ticket_num).count() > 0:
			return Response({'detail':{'message':'This Ticket Number is already Issued'},'status_code':'0'})
		serializer = AddZiraSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({'detail':serializer.data,'status_code':'1'})

		return Response({'detail':{'message':'Error'},'status_code':'0'})


@api_view(['GET','POST'])
def ziralist(request):
    context = {
            "request":request
            }
    a = zira.objects.all()
    serializer = AddZiraSerializer(a, many=True,context=context)
    resp3 = serializer.data
    a = {'Zira_List':resp3}
    return Response(a)

class SearchApi(APIView):
	serializer_class = SearchSerializer

	def post(self,request,*args,**kwargs):
		data = request.data
		ticket_num = data['ticket_num']
		try:
			a = zira.objects.get(ticket_num=ticket_num)
		except Exception as e:
			return Response({'detail':{'message':'This Ticket Number is Not Found'},'status_code':'0'})
		b = {}
		b['ticket_num'] = a.ticket_num
		b['issue_description'] = a.issue_description
		b['uploaded_by'] = a.uploaded_by
		b['date'] = a.date
		return Response(b)
		