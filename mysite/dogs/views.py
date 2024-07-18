from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

def index(request):
    return HttpResponse("Hello, World! You are at the polls index.")

# get a list of all dog breeds
def dogs_breeds_list(request):
    api_url = 'https://dog.ceo/api/breeds/list/all'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        breeds = data['message']
        result = {}
        
        for breed, sub_breeds in breeds.items():
            breed_name = breed[0].upper() + breed[1:]
            if len(sub_breeds) == 0:
                result[breed_name] = breed
            else:
                for sub_breed in sub_breeds:
                    sub_breed_name = sub_breed[0].upper() + sub_breed[1:]
                    result[breed_name + " " + sub_breed_name] = breed + "-" + sub_breed

        print(result)
        return JsonResponse(result)
    
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status = response.status_code)
    
# get a random image of a dog by breed
def dog_random_pic_by_breed(request, breed_name):
    breed_sub_breed = breed_name.replace('-','/')

    api_url = f'https://dog.ceo/api/breed/{breed_sub_breed}/images/random'

    print(api_url)


    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        img_url = data['message']
        result = {
            "image_url": img_url,
        }
        return JsonResponse(result)

    else:
        return JsonResponse({'error': "Failed to retrieve data"}, status = response.status_code)
    
# get a random image of a dog
def dog_random_pic(request):
    api_url = 'https://dog.ceo/api/breeds/image/random'

    print(api_url)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        img_url = data['message']
        result = {
            "image_url": img_url,
        }
        return JsonResponse(result)

    else:
        return JsonResponse({'error': "Failed to retrieve data"}, status = response.status_code)