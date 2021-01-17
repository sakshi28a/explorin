from django.shortcuts import render

def portfolio(request):
	return render(request, 'portfolio.html')

def accordian(request):
	return render(request, 'accordian.html')

def bill(request):
	return render(request, 'bill.html')

def flex(request):
	return render(request, 'flex.html')

def trial12(request):
	return render(request, 'trial12.html')

def weekly1(request):
	return render(request, 'weekly1.html')

# Create your views here.
