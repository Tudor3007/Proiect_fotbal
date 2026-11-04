from django.http import HttpResponse
from datetime import datetime
from urllib.parse import urlencode
from django.shortcuts import render

zile=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
luni=["Ianuarie","Februarie","Martie","Aprilie","Mai","Iunie","Iulie","August","Septembrie","Octombrie",
      "Noiembrie","Decembrie"]
accesari=[]


class Accesare:
    contor=0
    def __init__(self, ip_client, url, parametri=None):
        Accesare.contor=Accesare.contor+1
        self.id= Accesare.contor
        self.ip_client = ip_client
        self.url = url
        if parametri is None:
            parametri = {}
        self.parametri = parametri
        self.data = datetime.now()

    def lista_parametri(self):
        rezultat=[]
        for nume, valori in self.parametri.items():
            if len(valori)==1 and valori[0]=="":
                valoare=None
            elif len(valori)==1:
                valoare=valori[0]
            else:
                valoare=valori
            rezultat.append((nume, valoare))
        return rezultat

    def string_url(self):
        if len(self.parametri)==0:
            return self.url
        return self.url + "?" + urlencode(self.parametri,doseq=True)

    def pagina(self):
        bucati= self.url.split("echipament_fotbal/")
        return "/" + bucati[-1]

    def calculeaza_data(self, format="%A, %d %B %Y", tip=""):
        if tip=="zi":
            format="%A, %d %B %Y"
        elif tip=="timp":
            format = "%H:%M:%S"
        format = format.replace("%A", zile[self.data.weekday()])
        format = format.replace("%B", luni[self.data.month - 1])
        format = format.replace("%d", str(self.data.day))
        return self.data.strftime(format)


    def __str__(self):
        return(f"id: {self.id} \n"
              f"ip client: {self.ip_client} \n"
              f"string url: {self.string_url()} \n"
              f"pagina: {self.pagina()} \n"
              f"data: {self.calculeaza_data()} \n"
              f"lista parametri: {self.lista_parametri()} \n"
              )


def inregistreaza_accesare(request):
    acc=Accesare(request.ip_client, request.build_absolute_uri(request.path), dict(request.GET.lists()))
    accesari.append(acc)
    print(acc)
    return acc







def index(request):
    acc=inregistreaza_accesare(request)
    return render(request, "index.html")
def info(request):
    acc = inregistreaza_accesare(request)
    tip = request.GET.get("data", "")
    return render(request, "info.html", {"data_ora": acc.calculeaza_data("%A, %d %B %Y %H:%M:%S", tip=tip)})


def log(request):
    acc = inregistreaza_accesare(request)
    mesaj_nr=""
    mesaj_detalii=""
    accesari_param=request.GET.get("accesari")
    if accesari_param is not None:
        if accesari_param == "nr":
            mesaj_nr=(f"Numar accesari <br>"
                      f"Au fost {len(accesari)} accesari de la pornirea serverului")
        elif accesari_param == "detalii":
            mesaj_detalii=("Detalii accesari <br><ul>")
            for a in accesari:
                mesaj_detalii=mesaj_detalii+(f"<li> {a.calculeaza_data("%A, %d %B %Y %H:%M:%S")}</li>")
            mesaj_detalii=mesaj_detalii+"</ul>"

    ultimele= request.GET.get("ultimele")
    de_afisat=accesari
    mesaj=""
    if ultimele is not None:
        try:
            n= int(ultimele)
        except ValueError:
            return HttpResponse("<p> valoare nu este int </p>")
        if n>0:
            de_afisat=accesari[-n:]
        else:
            de_afisat=[]
        if n>len(accesari):
            mesaj=f"Exista doar {len(accesari)} accesari fata de {n} accesari cerute."

    valori_iduri=request.GET.getlist("iduri")
    dubluri= request.GET.get("dubluri") == "true"
    if valori_iduri:
        de_afisat=[]
        vazut=[]
        for valoare in valori_iduri:
            valoare=valoare.split(",")
            for a in valoare:
                try:
                    id_cerut= int(a)
                except ValueError:
                    continue
                if dubluri==False and id_cerut in vazut:
                    continue
                vazut.append(id_cerut)
                for b in accesari:
                    if b.id == id_cerut:
                        de_afisat.append(b)

    tabel_param=request.GET.get("tabel")
    tabel_html=""
    if tabel_param is not None:
        if tabel_param == "tot":
            tabel_html=(f"<table border=1>"
                        f"<tr> <th> id </th> <th> ip client </th> <th> url </th> <th> parametri </th> <th> data </th> </tr>")
            for a in de_afisat:
                tabel_html=tabel_html+(f"<tr><td>{a.id}</td> <td>{a.ip_client}</td> <td>{a.string_url()}</td>"
                                       f"<td>{a.parametri}</td> <td>{a.data}</td></tr>")
            tabel_html=tabel_html+"</table>"
        else:
            coloane=tabel_param.split(",")
            tabel_html=(f"<table border=1>"
                        f"<tr>")
            for a in coloane:
                tabel_html=tabel_html+(f"<th>{a}</th>")
            tabel_html=tabel_html+"</tr>"
            for a in de_afisat:
                tabel_html=tabel_html+(f"<tr>")
                for b in coloane:
                    tabel_html=tabel_html+(f"<td>{getattr(a,b,'')}</td>")
                tabel_html=tabel_html+"</tr>"
            tabel_html=tabel_html+"</table>"


    numarari={}
    for a in accesari:
        pagina=a.pagina()
        numarari[pagina]=numarari.get(pagina,0)+1
    pagina_max = max(numarari, key=numarari.get)
    pagina_min = min(numarari, key=numarari.get)

    sectiune_parametri=(f"<h2>Parametri</h2>"
                        f"Numar parametri: {len(acc.parametri)} <br>"
                        f"Nume parametri: {", ".join(acc.parametri.keys())}<br>")
    html=""
    for a in de_afisat:
        html=html+(f"<li>id: {a.id} <br>"
                   f"pagina: {a.pagina()} <br>"
                   f"data: {a.calculeaza_data("%A, %d %B %Y %H:%M:%S")}</li>")
    return render(request, "log.html", {
        "html": html,
        "mesaj": mesaj,
        "mesaj_nr": mesaj_nr,
        "mesaj_detalii": mesaj_detalii,
        "tabel_html": tabel_html,
        "sectiune_parametri": sectiune_parametri,
        "pagina_max": pagina_max,
        "pagina_min": pagina_min,
    })




def istoric(request):
    acc = inregistreaza_accesare(request)
    return render(request, "istoric.html")


def despre(request):
    acc = inregistreaza_accesare(request)
    return render(request, "despre.html")

def accesare(request,id):
    acc = inregistreaza_accesare(request)
    mesaj=""
    gasit=0
    for a in accesari:
        if a.id == int(id):
            mesaj=(f"<h2>Informatii despre accesarea cu id-ul: {id}</h2>"
                   f"id: {a.id} <br>"
                   f"ip_client: {a.ip_client} <br>"
                   f"url: {a.string_url()} <br>"
                   f"pagina: {a.pagina()} <br>"
                   f"data: {a.calculeaza_data("%A, %d %B %Y %H:%M:%S")} <br>"
                   f"parametri: {a.parametri} <br>")
            gasit=1
    if gasit==0:
        mesaj=f"Nu exista accesarea cu id-ul: {id}"
        return render(request, "accesare.html", {"mesaj": mesaj})
    else:
        return render(request, "accesare.html", {"mesaj": mesaj})

def produse(request):
    acc = inregistreaza_accesare(request)
    return render(request, "in_lucru.html")

def contact(request):
    acc = inregistreaza_accesare(request)
    return render(request, "in_lucru.html")

def cos_virtual(request):
    acc = inregistreaza_accesare(request)
    return render(request, "in_lucru.html")
