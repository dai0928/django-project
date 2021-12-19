from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from django.urls import reverse_lazy
from .models import *


class MainLesson(TemplateView):
    template_name = "main.html"


class Lesson1(TemplateView):
    template_name = "1_HTMLver.html"


class Lesson2(TemplateView):
    template_name = "2_rule.html"


class Lesson3(TemplateView):
    template_name = "3_langcode.html"


class Lesson4(TemplateView):
    template_name = "4_BODY.html"


class Lesson5(TemplateView):
    template_name = "5_symbol.html"


class Lesson6(TemplateView):
    template_name = "6_List1.html"


class Lesson7(TemplateView):
    template_name = "7_List2.html"


class Lesson8(TemplateView):
    template_name = "8_IMG.html"


class Lesson9(TemplateView):
    template_name = "9_Link.html"


class Lesson10(TemplateView):
    template_name = "10_table.html"


class Lesson11(TemplateView):
    template_name = "11_form.html"


class Css_Lesson(TemplateView):
    template_name = "howto_css.html"


class Python(TemplateView):
    template_name = "python.html"


class Python_Lesson(TemplateView):
    template_name = "howto_python.html"


class Search_name(CreateView):
    template_name = "search.html"
    model = SearchModel
    fields = ("text", )
    success_url = reverse_lazy("program:result")


def search_list(request):
    for word in SearchModel.objects.all():
        result1 = "Search_word:" + word.text
        url = "https://www.google.co.jp/search?q=" + word.text
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    next_page = browser.find_element_by_xpath("//a[@aria-label='Page 10']")
    next_page.click()
    div = browser.find_elements_by_class_name("yuRUbf")
    title1 = div[0].find_element_by_class_name("LC20lb")
    title2 = div[1].find_element_by_class_name("LC20lb")
    title3 = div[2].find_element_by_class_name("LC20lb")
    title4 = div[3].find_element_by_class_name("LC20lb")
    title5 = div[4].find_element_by_class_name("LC20lb")
    title = [title1, title2, title3, title4, title5]
    # print(type(title))
    # print(title)

    a_tag1 = div[0].find_element_by_tag_name("a")
    link1 = a_tag1.get_attribute('href')
    a_tag2 = div[1].find_element_by_tag_name("a")
    link2 = a_tag2.get_attribute('href')
    a_tag3 = div[2].find_element_by_tag_name("a")
    link3 = a_tag3.get_attribute('href')
    a_tag4 = div[3].find_element_by_tag_name("a")
    link4 = a_tag4.get_attribute('href')
    a_tag5 = div[4].find_element_by_tag_name("a")
    link5 = a_tag5.get_attribute('href')
    link = [link1, link2, link3, link4, link5]

    title_link = dict(zip(title, link))
    # print(list)
    # print(type(list))

    return render(request, "result.html", context={"result1": result1, "title_link": title_link})











