from django.shortcuts import render

# Create your views here.

#<FBV 스타일로 페이지 만들기>
#대문 페이지
def landging(request):
    return render(request, 'single_pages/landing.html')
#자기소개 페이지
def about_me(request):
    return render(request, 'single_pages/about_me.html')