from django.shortcuts import render
from django.urls import URLPattern
import csv, io
from movie.models import Movie_data
from movie.serializers import MovieDataSerializer
import datetime
from django.http import JsonResponse, HttpResponse
# Create your views here.


csv_columnname_arrayindex_mapper = {
    0 : "budget",
    1 : "homepage",
    2 : "original_language_code", 
    3 : "original_title",
    4 : "overview",
    5 : "release_date",
    6 : "revenue",
    7 : "runtime",
    8 : "status",
    9 : "title",
    10 : "rating",
    11 : "vote_count",
    12 : "production_company_id",
    13 : "genre_id",
    14 : "languages"
}


def parse_csv_data_to_dict(data):
    parsed_data_list = []
    for row in data:
        parsed_data = dict()
        for i in range(0,len(row)):
            key = csv_columnname_arrayindex_mapper[i]
            parsed_data[key] = row[i]
        parsed_data_list.append(parsed_data)
    return parsed_data_list


def movie_csv_parser(file_obj):
    csv_reader = csv.reader(file_obj)
    header = next(csv_reader)
    data = [row for row in csv_reader]
    return data


def bulk_create(data, model):
    bulk_data = []
    count = 0
    for i in range(0, len(data)):
        item = data[i]
        try:
            serializer = MovieDataSerializer(data=item)
            if serializer.is_valid():
                bulk_data.append(Movie_data(**serializer.validated_data))
            else:
                count += 1
                print(f"Error in serliazer record ********** {i} {serializer.error_messages} {serializer.errors}")
        except Exception as e:
            print(f"Error in record ************ {i}")
            print(str(e))
        
        if i%1000 == 999:
            print(f"Completed {i + 1} records")
    model.objects.bulk_create(bulk_data, batch_size = 5000)
    return



def upload_data(request):

    uploaded_file = request.FILES.get('input.csv')
    try:
        decoded_file = uploaded_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)  # Create a StringIO object
        parsed_data = movie_csv_parser(io_string)
        parsed_data_dict = parse_csv_data_to_dict(parsed_data)
        bulk_create(parsed_data_dict, Movie_data)
        return JsonResponse({"message" : "data successfully uploaded"}, status = 200)
    except Exception as e:
        print("Exception in upload_csv_files *************")
        print(str(e))
        return JsonResponse({"message" : "Error in uploading data" }, status = 500)



def view_moviedata(request):
    kwargs = dict()
    year_of_release = request.GET.get("year_of_release", None)
    if year_of_release:
        kwargs["release_date__year"] = year_of_release
    language = request.GET.get("language", None)
    if language:
        kwargs["original_language_code"] = language
    records_perpage = int(request.GET.get("records_perpage", 100))
    page_number = int(request.GET.get("page_number", 1))
    movie_data_full = Movie_data.objects.filter(**kwargs).order_by("-release_date", "-rating")
    first_record = records_perpage * (page_number - 1)
    last_record = records_perpage * page_number
    movie_data = movie_data_full[first_record : last_record]
    movie_data_json = MovieDataSerializer(movie_data, many = True).data
    return JsonResponse({"data": movie_data_json}, status = 200)


def test(request):
    return HttpResponse("it is working... ")

