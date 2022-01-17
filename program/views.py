from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from django.urls import reverse_lazy
from .models import SearchModel
from time import sleep


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
    url = "https://www.yahoo.co.jp/"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)

    # サーバーのChromeが立ち上がったまま次の処理が実行されるとChromeがクラッシュする為、tryでスクレイピング処理、finallyでブラウザの終了を記述した
    try:
        browser.set_window_size(1024, 768)
        browser.get(url)
        sleep(2)
        search_box = browser.find_element_by_class_name("_1wsoZ5fswvzAoNYvIJgrU4")
        search_box.send_keys(word.text)
        search_btn = browser.find_element_by_class_name("PHOgFibMkQJ6zcDBLbga8")
        search_btn.click()
        sleep(2)
        # browser.save_screenshot("page.png")
        div = browser.find_elements_by_class_name("Algo")
        title1 = div[0].find_element_by_class_name("sw-Card__titleMain")
        title2 = div[1].find_element_by_class_name("sw-Card__titleMain")
        title3 = div[2].find_element_by_class_name("sw-Card__titleMain")
        title4 = div[3].find_element_by_class_name("sw-Card__titleMain")
        title5 = div[4].find_element_by_class_name("sw-Card__titleMain")
        title = [title1, title2, title3, title4, title5]
        # # print(type(title))
        # # print(title)

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

        # return render(request, "result.html", context={"urls": urls, "result1": result1, "title": title})
        return render(request, "result.html", context={"result1": result1, "title_link": title_link})
    finally:
        browser.quit()











