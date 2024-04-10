from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .serializers import CompanySerializer, VacancySerializer
from .models import Company, Vacancy
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.
@require_http_methods(["GET"])
def get_companies(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_companies_by_id(request,id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return HttpResponse('Company not found')
    serializer = CompanySerializer(company, many = False)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_vacancies(request):
    vac = Vacancy.objects.all()
    serializer = VacancySerializer(vac, many=True)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_vacancy_by_id(request,id):
    try:
        vac = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return HttpResponse('Vacancy not found')
    serializer = VacancySerializer(vac, many=False)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_vacancies_by_companies_id(request,id):
    try:
        companys = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return HttpResponse('Company not found')
    vacancies = Vacancy.objects.filter(company=companys)
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

@require_http_methods(["GET"])
def get_vacancy_top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)
