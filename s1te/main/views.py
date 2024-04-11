from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page',
        'values': ['some', 'shishki', 'nasvay'],
        'obj': {
            'car': 'RX7',
            'grams': 500,
                     'money': '9999999BTC',
    }   }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

