"""Backend strony internetowej cały czas w budowie"""
import gc
from functools import wraps
from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file
from content_management import Content, python_content, gpu_content, likes_setter
from pymysql import escape_string as thwart
from passlib.hash import sha256_crypt
from wtforms import Form, validators, StringField, PasswordField, BooleanField
from dbconnect import connection
from flask_mail import Mail, Message

APP = Flask(__name__)
APP.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='biuro.tkgf@gmail.com',
    MAIL_PASSWORD='huberttostuprocentowydebil'
)
mail = Mail(APP)

GROUP_LIST = Content()
PYTHON_ARTICLES = python_content()
GPU_ARTICLES = gpu_content()


def login_required(func):
    """Wymaganie logowania"""

    @wraps(func)
    def wrap(*args, **kwargs):
        """Nie mam do końca pojęcia jak to działa"""
        if 'logged_in' in session:
            return func(*args, **kwargs)
        flash("Musisz być zalogowany.")
        return redirect(url_for('login'))

    return wrap


@APP.route("/logout/")
@login_required
def logout():
    """Wyloguj się czyszcząc sesję"""
    session.clear()
    flash("Zostałeś poprawnie wylogowany.")
    gc.collect()
    return redirect(url_for('homepage'))


@APP.route('/register/', methods=["GET", "POST"])
def register():
    """Wyślij nowe dane do bazy danych jeżeli są poprawne"""
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            con, conn = connection()
            username_quantity = con.execute("SELECT * FROM users WHERE username = (%s)",
                                            (thwart(username)))
            if int(username_quantity) > 0:
                flash('Ta nazwa użytkowania jest już zajęta, proszę wybierz inną.')
                return render_template('register.html', form=form)
            con.execute("INSERT INTO users (username, password, email, tracking) VALUES "
                        "(%s, %s, %s, %s)", (thwart(username), thwart(password),
                                             thwart(email), thwart('/homepage/')))
            conn.commit()
            flash("Dzięki za rejestrację!")
            con.close()
            conn.close()
            gc.collect()
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('homepage'))

        return render_template('register.html', form=form)
    except Exception as error:
        flash(error)
        return redirect(url_for('main'))


class RegistrationForm(Form):
    """Forma do rejestracji"""
    username = StringField('Nazwa użytkowania', [validators.Length(min=4, max=20)])
    email = StringField('Adres email', [validators.Length(min=6, max=50)])
    password = PasswordField('Hasło',
                             [validators.DataRequired(),
                              validators.EqualTo('confirm',
                                                 message='Hasła muszą być jednakowe')])
    confirm = PasswordField('Powtórz hasło')
    accept_tos = BooleanField('Akceptuję Warunki użytkowania i Politykę prywatności'
                              '(zaktualizowana 17 stycznia 2018r.)', [validators.Required()])


@APP.route('/login/', methods=["GET", "POST"])
def login():
    """Wysyła zapytanie do bazy danych o login użytkownika a następnie porównuje
	jego zhashowane hasło z hashem z bazy danych"""
    try:
        con, conn = connection()
        if request.method == "POST":
            con.execute("SELECT * FROM users WHERE username = (%s)",
                        thwart(request.form['username']))
            data = con.fetchone()['password']
            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash("Jesteś zalogowany jako  " + session['username'])
                return redirect(url_for('homepage'))
            else:
                flash("Niepoprawne hasło")
        gc.collect()
        return redirect(url_for('homepage'))
    except Exception:
        flash("Niepoprawna nazwa użytkowania")
        return redirect(url_for('homepage'))


@APP.route('/filipwachowiak/')
def filipwachowiak():
    return render_template("filipwachowiak.html")


@APP.route('/plakatMT/')
def downloads():
    """PDF na EDB Mateusza Targowskiego - nie usuwać"""
    return send_file('static/1_MARCA-plakat.pdf', as_attachment=True,
                     attachment_filename='Plakat Mateusz Targowski.pdf')


@APP.route('/contact/', methods=["GET", "POST"])
def team():
    content = ""
    try:
        if request.method == "POST":
            content = "Main topic: "
            if request.form.get('programming'):
                content += request.form['programming'] + " "
            else:
                content += "off "
            if request.form.get('net'):
                content += request.form['net'] + " "
            else:
                content += "off "
            if request.form.get('hardware'):
                content += request.form['hardware'] + " "
            else:
                content += "off "
            if request.form.get('mobile'):
                content += request.form['mobile'] + " "
            else:
                content += "off "
            if request.form.get('os'):
                content += request.form['os'] + " "
            else:
                content += "off "
            if request.form.get('other'):
                content += request.form['other'] + " "
            else:
                content += "off "
            if request.form.get('other_content'):
                content += request.form['other_content'] + "\n"
            else:
                content += "off\n"

            content += "Programming: "
            if request.form.get('pl') and request.form.get('programming') == "programming":
                content += request.form['pl'] + " "
            else:
                content += "off "
            if request.form.get('pl') == "otherP":
                content += request.form['otherP_content'] + "\n"
            else:
                content += "\n"
            content += "Web: "
            if request.form.get('s') and request.form.get('net') == "net":
                content += request.form['s'] + " "
            else:
                content += "off "
            if request.form.get('s') == "otherS":
                content += request.form['otherS_content'] + "\n"
            else:
                content += "\n"
            content += "Hardware: "
            if request.form.get('h') and request.form.get('hardware') == "hardware":
                content += request.form['h'] + " "
            else:
                content += "off "
            if request.form.get('h') == "otherH":
                content += request.form['otherH_content'] + "\n"
            else:
                content += "\n"
            content += "Mobile: "
            if request.form.get('pm') and request.form.get('mobile') == "mobile":
                content += request.form['pm'] + " "
            else:
                content += "off "
            if request.form.get('pm') == "otherPM":
                content += request.form['otherPM_content'] + "\n"
            else:
                content += "\n"
            content += "OS: "
            if request.form.get('so') and request.form.get('os') == "os":
                content += request.form['so'] + " "
            else:
                content += "off "
            if request.form.get('so') == "otherSO":
                content += request.form['otherSO_content'] + "\n"
            else:
                content += "\n"
            email = request.form.get("email")
            if request.form['desc'] == "Napisz coś o sobie (chociażby imię i nazwisko)":
                raise Exception("Serio, napisz coś o sobie...")
            content += "Description: " + request.form['desc']

            try:
                msg = Message(email,
                              sender="biuro.tkgf@gmail.com",
                              recipients=["wachowiakf@gmail.com"])
                msg.body = content
                mail.send(msg)
                return redirect(url_for("team_success"))
            except Exception as e:
                flash(str(e))
                return redirect(url_for("team"))
        else:
            return render_template("team.html", content=content)
    except Exception as e:
        flash(str(e))
        return redirect(url_for("team"))


@APP.route('/team/success/')
def team_success():
    return render_template("teamSuccess.html", content="Sukces, dziękujemy za zgłoszenie.")


@APP.route('/')
def homepage():
    """Wyświetla stronę z działami i tematami"""
    return render_template("main.html",
                           title="Zero jeden - myślimy binarnie",
                           groupList=GROUP_LIST)


@APP.route('/lan/')
def lan():
    """Wyświetla dział sieci lokalnych"""
    return render_template("lan.html")


@APP.route('/web/')
def web():
    """Wyświetla dział Internet"""
    return render_template("web.html")


@APP.route('/kotlin/')
def kotlin():
    """Wyświetla dział Kotlin"""
    return render_template("kotlin.html", title="Kotlin",
                           imgSource="http://tkgf.nazwa.pl:5003/static/images/kotlin.jpg")


@APP.route('/java/')
def java():
    """Wyświetla dział Java"""
    return render_template("java.html", title="Java",
                           imgSource="http://tkgf.nazwa.pl:5003/static/images/java.jpg")


@APP.route('/python/')
def python():
    """Wyświetla dział Python"""
    likes = []
    for article in PYTHON_ARTICLES:
        likes.append(likes_setter(article))
    return render_template("python.html", title="Python",
                           imgSource="http://tkgf.nazwa.pl:5003/static/images/python.jpg",
                           articles=PYTHON_ARTICLES,
                           likes=likes)


@APP.route('/cpp/')
def cpp():
    """Wyświetla dział C++"""
    return render_template("cpp.html", title="C/C#/C++",
                           imgSource="http://tkgf.nazwa.pl:5003/static/images/c++.jpg")


@APP.route('/tomaszlakomy/')
def tom():
    """Wyświetla stronę Tomka"""
    return render_template("/tl/index.html")


@APP.route('/tomaszlakomy/<podstrona>/')
def tome(podstrona):
    """Wyświetla stronę Tomka"""
    return render_template("/tl/" + podstrona)


@APP.route('/adamkorba/')
def adamk():
    return render_template("/adamk/strona.html")


@APP.route('/adamkorba/<podstrona>')
def adamk2(podstrona):
    return render_template("/adamk/" + podstrona)


@APP.route('/gpu/')
def gpu():
    """Wyświetla dział GPU"""
    likes = []
    for article in GPU_ARTICLES:
        likes.append(likes_setter(article))
    return render_template("gpu.html", title="Karty graficzne",
                           imgSource="http://tkgf.nazwa.pl:5003/static/images/gpu.jpg",
                           articles=GPU_ARTICLES,
                           likes=likes)


@APP.route('/<topic>/articles/<article_name>/', defaults={"action": None})
@APP.route('/<topic>/articles/<article_name>/<action>/')
def article_view(topic, article_name, action):
    """Wyświetla <artykuł> z działu <topic>"""
    article_title = None
    if topic == "gpu":
        for article in GPU_ARTICLES:
            if article[3] == "/gpu/articles/" + article_name:
                if action == "like" and "logged_in" in session:
                    likes_setter(article, session['username'])
                    return redirect("/" + topic + "/articles/" + article_name)
                elif action == "like":
                    article_likes = likes_setter(article)
                    flash("Musisz być zalogowany aby polubić ten artykuł")
                else:
                    article_likes = likes_setter(article)

                article_title = article[0]
                article_text = article[2]
                article_image = article[4]
    elif topic == "python":
        for article in PYTHON_ARTICLES:
            if article[3] == "/python/articles/" + article_name:
                if action == "like" and "logged_in" in session:
                    likes_setter(article, session['username'])
                    return redirect("/" + topic + "/articles/" + article_name)
                elif action == "like":
                    article_likes = likes_setter(article)
                    flash("Musisz być zalogowany aby polubić ten artykuł")
                else:
                    article_likes = likes_setter(article)

                article_title = article[0]
                article_text = article[2]
                article_image = article[4]
    if article_title:
        return render_template(topic + "_article_view.html",
                               title=article_title,
                               text=article_text,
                               image=article_image,
                               likes=article_likes)
    else:
        return render_template(topic + "_article_view.html",
                               title="Zero Jeden 404",
                               text="Nie znaleźliśmy takiego artykułu",
                               image="https://msdn.microsoft.com/dynimg/IC725763.png")


@APP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


APP.secret_key = "klawy sekret"

if __name__ == "__main__":
    APP.run(debug=True, host='77.55.221.165', port=5003)
