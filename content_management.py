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

kotlin_articles = (("Dlaczego Kotlin jest przyszłością Androida",
                    "Czyli trochę o tym, dlaczego warto przesiąść się z Javy na Kotlin",
                    "<h5>Artykuł w budowie</h5> Od dłuższego już czasu (a dokładniej od maja 2017 roku) Kotlin jest wspierany przez Google jako " +
                    "oficjalny język programowania na Androidzie. Jednak co takiego się stało, że Google postanowił " +
                    "wprowadzić oficjalnie drugi androidowy język?"+
                    """ <div align="center"><img style="width: 20vw; padding-top:10px;padding-bottom:10px" src="http://tkgf.nazwa.pl:5003/static/images/articles/kotlin/kotlin_eats_java.png"></div> """ +
                    "<ul><li>Kod napisany w Kotlinie jest zwykle dużo "+
                    "<b>czytelniejszy</b> od tego napisanego w Javie, co przede wszystkim umożliwia prosty "+
                    "start z Androidem dla żółtodziobów, ale również umożliwia łatwiejsze zrozumienie naszego kodu "+
                    "przez innych programistów </li><li>Kotlin można wysoce <b>zintegrować</b> z Javą. Chcąc "+
                    "zbudować naszą aplikację nie trzeba jej całkowicie przebudowywać, można napisać część"+
                    "w Kotlinie, a resztę pozostawić w Javie. Natomiast klasy Kotlina czerpią prosto z API Javy."+
                    "</li><li>Sam język nie jest jedynie chwilowym zachwytem. Wpiera go Google, a rozwija firma "+
                    "JetBraint, więc o przyszłość Kotlina nie ma się na razie co martwić</li></ul> Największą "+
                    "wadą Kotlina wydaje się być mała społeczność i mała ilość kodu jak dotąd napisanego. Jednak "+
                    "developerzy zachwalają Kotlina pomimo tego, a samego wprowadzenia nowego języka raczej nie hejtuje nikt."+
                    " Nie ma się temu co dziwić, w końcu nikogo to nie ogranicza, a daje wybór(ja tam wolę mieć wybór niż go "+
                    "nie mieć, nie wiem jak wy). Spójrzmy na bardziej konkretne rzeczy, które "+
                    "wprowadza Kotlin <ul><li><b>Null safety</b> - rzecz, której brak był jednym z większych koszmarów wszystkich"+
                    "osób używających Javy na Androidzie i nie tylko. W dużym skrócie null safety pozwala nam zedeklarować czy "+
                    "konkretna zmienna może być nullem, czy też nie. Oraz wiele innych wygodnych obsłużeń nulla, tak by "+
                    "programista nie musiał stykać się zbyt często ze znienawidzonym <b>NullPointerException</b>em.</li>"+
                    "<li>Sam Kotlin jest multiparadygmatywny co oznacza, że możesz pisać na przykład zarówno funkcyjnie "+
                    "jak i klasowo</li></ul> Nieraz denerwowała Cię Java? Kotlin to powiew świeżości dla starego wyjadacza "+
                    "Javy. Rozwiązuje również wiele innych błędów i problemów Javy, które nie mogły zostać rozwiązane głownie "+
                    "ze względu na to, że Java jest Javą i Javą pozostanie. <b>Dlaczego więc nie spróbować Kotlina już dziś?"+
                    ".</b> No już jazda,"+""" <a href="https://kotlinlang.org/docs/reference/">"""+"dokumentacja</a> czeka"+
                    """<br><h5 style="text-align:right">Autor: Filip Wachowiak</h5>""",
                    "/kotlin/articles/Dlaczego Kotlin jest przyszłością Androida",
                    "http://tkgf.nazwa.pl:5003/static/images/articles/kotlin/kotlin_eats_java.png"),
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


def likes_setter(article, username):
    with open('../zero-jeden/comments/'+article[0]+'.txt', 'a+') as file:
        file.seek(0)
        data = file.read().splitlines()
        if username not in data and username is not '':
            file.write(username+'\n')

def likes_getter(article):
    with open('../zero-jeden/comments/'+article[0]+'.txt', 'a+') as file:
        file.seek(0)
        data = file.read().splitlines()
    likes = len(data)
    return likes

def gpu_content():
    return gpu_articles

def kotlin_content():
    return kotlin_articles