# Lista cerinte -> unde sunt implementate
Proiect: Goal Gear (echipament de fotbal) - Pencea Tudor-Florian, grupa 241
(V = echipament_fotbal/views.py, S = Proiect_fotbal/settings.py, T = templates/, CSS = static/css/nav.css)

## LABORATOR 1
| Cerinta | Fisier : linii |
|---|---|
| Proiect + aplicatie, aplicatia inregistrata | S : 40 (INSTALLED_APPS) |
| Limba romana + ora Romaniei | S : 109, 111 |
| Rutele proiectului (include aplicatia) | Proiect_fotbal/urls.py : 22-23 |
| Rutele aplicatiei | echipament_fotbal/urls.py : 6-14 |
| Pagina principala cu descrierea | V : 78-80 (index) + T/index.html : 8-15 |
| Pagina /info, titlu tab + heading | V : 81-84 (info) + T/info.html : 3-5, 8 |
| Sectiunea "Data si ora" | T/info.html : 9-12 |
| Data in limba romana | V : 6-8 (liste zile/luni) + V : 45-54 (calculeaza_data) |
| Clasa Accesare (id auto, ip, url, parametri={}, data) | V : 12-22 (contor = proprietate de clasa, parametri=None) |
| lista_parametri() | V : 24-34 |
| string_url() | V : 36-39 (urlencode cu doseq=True) |
| pagina() | V : 41-43 |
| calculeaza_data(format, tip) - format implicit, refolosit in /info | V : 45-54 |
| /info?data=zi si /info?data=timp | V : 83-84 + V : 46-49 |
| Middleware pentru IP | echipament_fotbal/middleware.py : 1-15 + S : 51 |
| __str__ + afisare in consola la fiecare accesare | V : 56-63 + V : 66-70 (inregistreaza_accesare, print) |

## LABORATOR 2 - TASK 1
| Cerinta | Fisier : linii |
|---|---|
| Lista tuturor accesarilor (globala) | V : 9 + V : 66-70 (append) |
| Pagina /log cu toate cererile | V : 87-188 + T/log.html |
| ultimele=n (+ eroare daca nu e int) | V : 102-113 (try/except, slicing [-n:]) |
| Mesaj "Exista doar k accesari fata de n accesari cerute" | V : 114-115 |
| accesari=nr | V : 93-95 |
| accesari=detalii (lista neordonata cu data si ora) | V : 96-100 |
| iduri (de mai multe ori, separate prin virgula) + dubluri | V : 117-134 (getlist, split, vazut, continue) |
| tabel=tot / tabel=id,url | V : 136-158 (getattr) |
| Sectiunea "Parametri" (cati + nume) | V : 168-170 |
| Pagina cea mai / cea mai putin accesata | V : 161-166 (dictionar de numarare, max/min cu key) |
| Paginile /istoric si /despre | V : 190-197 + T/istoric.html, T/despre.html |
| re_path /accesare[id] | echipament_fotbal/urls.py : 11 + V : 199-217 |

## LABORATOR 2 - TASK 2
| Cerinta | Fisier : linii |
|---|---|
| Template de baza (header, main, footer) | T/baza.html |
| Pagina principala extinde baza (min. 3 sectiuni) | T/index.html : 1, 8-29 |
| Meniu cu submeniu, linkuri cu {% url %} | T/baza.html : 12-26 |
| Submeniu catre sectiuni de pagina (#promotii, #program) | T/baza.html : 16-17 |
| nav.css in static, meniu derulant | CSS : 1-32 (nav ul ul display:none, li:hover > ul display:block) |
| Alte reguli de stil + responsive | CSS : 34-62 (body, main, header, img, footer) + 63-67 (@media) |
| Folder static pe subfoldere (css, imagini) | static/css, static/imagini + S : 121-122 |
| Imagine in principala si despre cu {% static %} | T/index.html : 9 + T/despre.html : 24 |
| IP in footer (middleware) | T/baza.html : 34 |
| Context processor cu datele firmei din settings | S : 134-141 (FIRMA) + echipament_fotbal/context_processors.py + S : 67 + T/baza.html : 35-41 |
| Toate paginile pe template-uri care extind baza | T/info.html, log.html, despre.html, istoric.html, accesare.html |
| in_lucru.html + view-uri pentru paginile neimplementate | T/in_lucru.html + V : 219-229 |
| Sectiunea "Continut" | documentatie |

## LABORATOR 2 - TASK 3
| Cerinta | Unde |
|---|---|
| Diagrama bazei de date + descriere | documentatie |
