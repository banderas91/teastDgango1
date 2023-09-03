from django.shortcuts import render
import logging
logger = logging.getLogger('main')
logging.basicConfig(filename='myapp.log', level=logging.INFO)

def index(request):
  html = "<h1>Главная страница</h1>"   

  return render(request, 'index.html', {'html': html})

def about(request):
  html = "<h1>Обо мне</h1>"
  
  return render(request, 'about.html', {'html': html})




def index(request):
  html = """<h1>Главная страница</h1> 
              <p>Привет, это мой первый проект Django!</p>"""
  
  return render(request, 'index.html', {'html': html})

logger.info('Отображена главная страница')
  
def about(request):
  html = """<h1>Обо мне</h1>
             <p>Меня зовут Антон, я изучаю Django</p>""" 
   
  return render(request, 'about.html', {'html': html})

logger.info('Отображена страница "Обо мне"')