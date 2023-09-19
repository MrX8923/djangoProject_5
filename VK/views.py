from django.shortcuts import render
from VK.forms_classes import *
from random import choice
from string import ascii_letters
import json


def index(req):
    data: dict = {'title': 'Главная'}
    return render(req, 'index.html', context=data)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            job = request.POST['job']
            age = request.POST['age']
            email = request.POST['email']
            lang = request.POST['lang']
            mate = request.POST['mate']
            color = request.POST['color']
            age_18 = request.POST.get('age_18')
            text = request.POST['text']
            img_obj = request.FILES.get('img')

            if age_18 is None:
                return render(request, 'age_18.html', context={'title': '18+'})

            if img_obj is not None:
                with open(f'VK/static/media/{img_obj.name}', 'wb+') as file:
                    file.write(img_obj.read())

            data = {
                'page_content': {
                    'Имя': name if name != '' else 'Нет данных',
                    'Работа': job if job != '' else 'Нет данных',
                    'Возраст': age if age != '' else 'Нет данных',
                    'email': email if email != '' else 'Нет данных',
                    'Язык': lang,
                    'Помощники': mate,
                },
                'text': text,
                'color': color,
                'age_18': age_18,
                'img_path': f'media/{img_obj.name}' if img_obj is not None else 'media/no_img.jpg'
            }

            json_key = ''.join([choice(ascii_letters) for _ in range(10)])
            try:
                with open('VK/json_files/persons.json', 'r') as file:
                    temp: dict = json.load(file)

                temp.update({json_key: data})

                with open('VK/json_files/persons.json', 'w') as file:
                    json.dump(
                        temp,
                        file,
                        indent=2
                    )

            except Exception as exc:
                print(exc)
                with open('VK/json_files/persons.json', 'w') as file:
                    json.dump(
                        {json_key: data},
                        file,
                        indent=2
                    )

            return render(request, 'final.html', context={
                'title': 'Регистрация завершена',
                'data': data
            }
                          )

    form = RegistrationForm(request.POST, request.FILES)
    data = {'title': 'Регистрация', 'form': form}
    return render(request, 'form.html', context=data)
