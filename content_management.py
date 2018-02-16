import json


def Content():
    topic_dict = (("Programowanie", (
        ("Python", "/python/", "http://tkgf.nazwa.pl:5003/static/images/python.jpg"),
        ("Java", "/java/", "http://tkgf.nazwa.pl:5003/static/images/java.jpg"),
        ("C++", "/cpp/", "http://tkgf.nazwa.pl:5003/static/images/c++.jpg"),
        ("Kotlin", "/kotlin/", "http://tkgf.nazwa.pl:5003/static/images/kotlin.jpg"))),

                  ("Sieci", (
                      ("Sieci lokalne", "/lan/", "http://tkgf.nazwa.pl:5003/static/images/"),
                      ("Internet", "/web/", "http://tkgf.nazwa.pl:5003/static/images/"))),

                  ("Hardware", (
                      ("Procesory", "/cpu/", "http://tkgf.nazwa.pl:5003/static/images/"),
                      ("Karty graficzne", "/gpu/", "http://tkgf.nazwa.pl:5003/static/images/gpu.jpg"),
                      ("Dyski", "/disks/", "http://tkgf.nazwa.pl:5003/static/images/"))))
    return topic_dict


python_articles = (("Tytuł artykułu",
                    "opis artykułu max 70 litere fagawg daywhg dkgawd kyjhga kywfg bawyk jyfge ajfyg ajfga yegff yjgfh auye gfja yghfe aygfu ysgu gyksr gykrs dhiu",
                    "treść artykułu",
                    "/python/articles/link_do_artykulu",
                    "http://tkgf.nazwa.pl:5003/static/images/articles/article.jpg",
                    ()),
                   ("Tytuł artykułu 2", "opis artykułu max 70 liter",
                    "treść artykułu: Właśnie tutaj znajduje się treść artykułu " +
                    "pisana o pierwszej w nocy przeze mnie, Filipa Wachowiaka." +
                    "Właśnie oglądam sobie jak akademia Clutch Gaming bawi się " +
                    "z akademią Counter Logic Gaming. W 35 minucie są 32 zabójstwa" +
                    ", ogólnie zabawa prawie jak w bronzie. W 38 minucie CLGA zgarnęło" +
                    " Barona. Gra wygląda na praktycznie zakończoną ale zobaczmy do końca" +
                    "Koniec gry!!! Już minutę później CLGA wygrywa mimo wcześniejszych " +
                    "trzec przegranych i ani jednej wygranej przeciw CGA z dwona wygranymi" +
                    "wcześniej i jedną porażką. CLGA wygrało jednak w klasyfikacji generalnej" +
                    "Clutch Gaming Academy jest nadal wyżej niż Counter Logic Gaming Academy.",
                    "/python/articles/link_do_artykulu_2",
                    "http://tkgf.nazwa.pl:5003/static/images/articles/article2.jpg"
                    )
                   )

gpu_articles = (("Nowy TITAN już nie do gier",
                 "TITAN V",
                 "„Najpotężniejsza, jaką kiedykolwiek stworzono”" +
                 "karta została właśnie zaprezentowana. I… w sumie tyle, nic nowego. Ten wyścig trwał, trwa i trwać będzie. Możemy" +
                 " jednak przewidzieć owoce roku 2018-ego jeśli chodzi o karty graficzne. A jeśli chodzi o te od firmy Nvidia to " +
                 "mamy sporo zmian. <br>W nowej karcie wreszcie została użyta architektura Volta (od której karta zawdzięcza nazwę)." +
                 " Architektura ta przeznaczona jest przede wszystkim dla AI i do deep learning. Żeby to jeszcze bardziej podkreślić," +
                 " producent usunął „Geforce GTX” sprzed nazwy karty, która od lat była dość mocno połączona z serią TITAN. Mimo tego," +
                 " że karta nie jest przeznaczona do gier, to i tak pobija wszystkie rankingi. Póki co. Miejmy nadzieję, że niedługo" +
                 " znów zobaczymy Voltę, ale tym razem w gamingowej odsłonie. <br>Jeśli jest Volta, to muszą być i rdzenie Tensor. " +
                 "Ulepszona metoda przetwarzania macierzy będzie więc dostępna. Według producenta nowy sposób jest dwunastokrotnie " +
                 "szybszy od Pascala, dzięki wydajności połowicznej precyzji. Wydajność podwójnej precyzji też wzrosła, aż do 6,9 TFLOPS." +
                 """ <img style="width: 90vw; padding-top:10px;padding-bottom:10px" src="http://tkgf.nazwa.pl:5003/static/images/articles/hardware/gpu/titanv.jpg"> """ +
                 "Jak już jesteśmy przy rdzeniach, to rdzenie CUDA nadal są, spowodowały zmniejszenie taktowania i jest ich więcej " +
                 "- 5120, czyli o ponad 1200 więcej od poprzednika. Sama karta wykorzystuje już wersję CUDA 7.0.<br>" +
                 "Nvidia poszła za ciosem. Tak jak w Quadro GP100 tak i w TITAN V mamy pamięć HBM2, czyli standard pamięci" +
                 " opracowany przede wszystkim przez firmę AMD! Wielkość została natomiast taka jak wcześniej, czyli 12GB.<br>" +
                 "Dzięki jeszcze większej liczby tranzystorów (21 milionów), karta TITAN V ma rekordową moc obliczeniową w" +
                 " wysokości 110 TFLOPS! Zatem mamy możliwość stworzenia naprawdę potężnej maszyny, gdy połączymy kilka kart" +
                 " dzięki SLI… albo i nie, bo nowy TITAN nie ma już takiego wsparcia. Powód tego jest taki, że w przypadku tworzenia" +
                 " sieci neuronowych prościej jest je trenować na jednej karcie. A przecież karta ma do tego służyć.<br>" +
                 "Tak rozpoczęliśmy nowy rok, jeśli chodzi o rynek kart graficznych. Wszyscy fani głębokiego uczenia oraz " +
                 """akceleracji GPU mogą czuć się na razie nasyceni. Warto jednak poczekać co przyniesie nam ten rok.<br><h5 style="text-align:right">Autor: Patryk Niedźwiedziński</h5>""",
                 "/gpu/articles/Nowy TITAN już nie do gier",
                 "http://tkgf.nazwa.pl:5003/static/images/articles/hardware/gpu/titanv.jpg"
                 ),
                )


def python_content():
    return python_articles


def likes_setter(article, username=''):
    likes = 0
    for python_title in python_articles:
        if article[0] == python_title[0]:
            with open('../zero-jeden/comments/'+article[0]+'.txt', 'a+') as file:
                file.seek(0)
                data = file.read().splitlines()
                if username not in data and username is not '':
                    file.write(username+'\n')
                likes = len(data)

    for gpu_title in gpu_articles:
        if article[0] == gpu_title[0]:
            with open('../zero-jeden/comments/'+article[0]+'.txt', 'r+') as file:
                file.seek(0)
                data = file.read().splitlines()
                if username not in data and username is not '':
                    file.write(username + '\n')
                likes = len(data)
    return likes



def gpu_content():
    return gpu_articles
