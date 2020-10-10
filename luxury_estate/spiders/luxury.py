# encoding=utf8


import scrapy
from bs4 import BeautifulSoup
import requests
import scrapy
import random
import json
import re
#from unidecode import unidecode
import csv
import datetime


class Leboncoin_Spider(scrapy.Spider):
    today = datetime.date.today()
    name_variable = 'luxury_' + (today.strftime("%Y_%m_%d"))
    name = name_variable
    #name = 'luxury_2020_09_10'
    start_urls = ['https://fr.luxuryestate.com/france']

    def parse(self, response):

        for i in range(1, 3177):
            url = 'https://fr.luxuryestate.com/france?pag={0}'.format(str(i))
            yield scrapy.Request(url=url, callback=self.parse_page)

        for i in range(1, 186):
            url = 'https://fr.luxuryestate.com/en-location/france?sort=relevance&pag={0}'.format(
                str(i))
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        hrefs = soup.findAll("li", {"class": "search-list__item"})

        for a in hrefs:
            url = a.find("div", {"class": "details"}).find(
                "div", {"class": "details_title"}).find("a").get("href")
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        itm = {"ANNONCE_LINK": "",
               "FROM_SITE": "",
               "ID_CLIENT": "",
               "ANNONCE_DATE": "",
               "ACHAT_LOC": "",
               "SOLD": "",
               "MAISON_APT": "",
               "CATEGORIE": "",
               "NEUF_IND": "",
               "NOM": "",
               "ADRESSE": "",
               "CP": "",
               "VILLE": "",
               "QUARTIER": "",
               "DEPARTEMENT": "",
               "REGION": "",
               "PROVINCE": "",
               "ANNONCE_TEXT": "",
               "ETAGE": "",
               "NB_ETAGE": "",
               "LATITUDE": "",
               "LONGITUDE": "",
               "M2_TOTALE": "",
               "SURFACE_TERRAIN": "",
               "NB_GARAGE": "",
               "PHOTO": "",
               "PIECE": "",
               "NB_CHAMBRE": "",
               "PISCINE": "",
               "PRIX": "",
               "PRIX_M2": "",
               "URL_PROMO": "",
               "STOCK_NEUF": "",
               "PAYS_AD": "",
               "PRO_IND": "",
               "SELLER_TYPE": "",
               "MINI_SITE_URL": "",
               "MINI_SITE_ID": "",
               "AGENCE_NOM": "",
               "AGENCE_ADRESSE": "",
               "AGENCE_CP": "",
               "AGENCE_VILLE": "",
               "AGENCE_DEPARTEMENT": "",
               "EMAIL": "",
               "WEBSITE": "",
               "AGENCE_TEL": "",
               "AGENCE_TEL_2": "",
               "AGENCE_TEL_3": "",
               "AGENCE_TEL_4": "",
               "AGENCE_FAX": "",
               "AGENCE_CONTACT": "",
               "PAYS_DEALER": "",
               "FLUX": "",
               "SIREN": "",
               }
        ANNONCE_LINK = ""
        FROM_SITE = ""
        ID_CLIENT = ""
        ANNONCE_DATE = ""
        ACHAT_LOC = ""
        SOLD = ""
        MAISON_APT = ""
        CATEGORIE = ""
        NEUF_IND = ""
        NOM = ""
        ADRESSE = ""
        CP = ""
        VILLE = ""
        QUARTIER = ""
        DEPARTEMENT = ""
        REGION = ""
        PROVINCE = ""
        ANNONCE_TEXT = ""
        ETAGE = ""
        NB_ETAGE = ""
        LATITUDE = ""
        LONGITUDE = ""
        M2_TOTALE = ""
        SURFACE_TERRAIN = ""
        NB_GARAGE = ""
        PHOTO = ""
        PIECE = ""
        NB_CHAMBRE = ""
        PISCINE = ""
        PRIX = ""
        RIX_M2 = ""
        URL_PROMO = ""
        STOCK_NEUF = ""
        PAYS_AD = ""
        PRO_IND = ""
        SELLER_TYPE = ""
        MINI_SITE_URL = ""
        MINI_SITE_ID = ""
        AGENCE_NOM = ""
        AGENCE_ADRESSE = ""
        AGENCE_CP = ""
        AGENCE_VILLE = ""
        AGENCE_DEPARTEMENT = ""
        EMAIL = ""
        WEBSITE = ""
        AGENCE_TEL = ""
        AGENCE_TEL_2 = ""
        AGENCE_TEL_3 = ""
        AGENCE_TEL_4 = ""
        AGENCE_FAX = ""
        AGENCE_CONTACT = ""
        PAYS_DEALER = ""
        FLUX = ""
        SIREN = ""

        ANNONCE_LINK = response.url
        FROM_SITE = "https://fr.luxuryestate.com/"
        ID_CLIENT = ANNONCE_LINK.split("/")[-1].split("-")[0]
        for i in ID_CLIENT:
            if i.isdigit() == False:
                ID_CLIENT = ID_CLIENT.replace(i, "")

        features = soup.find("div", {"class": "general-features"}).findAll(
            "div", {"class": "item-inner short-item feat-item"})

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Publié le":
                    DATE = i.find("div", {"class": "single-value"}).get_text()
                    for i in DATE:
                        if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                            DATE = DATE.replace(i, " ")
                    DATE = DATE.strip()
                    jour = DATE.split(" ")[0]
                    m = DATE.split(" ")[1]
                    annee = DATE.split(" ")[2]
                    print(jour)
                    print(m)
                    print(annee)

                    if m == "janvier":
                        mois = "01"

                    elif m == "février":
                        mois = "02"

                    elif m == "mars":
                        mois = "03"

                    elif m == "avril":
                        mois = "04"

                    elif m == "mai":
                        mois = "05"

                    elif m == "juin":
                        mois = "06"

                    elif m == "juillet":
                        mois = "07"

                    elif m == "août":
                        mois = "08"

                    elif m == "septembre":
                        mois = "09"

                    elif m == "octobre":
                        mois = "10"

                    elif m == "novembre":
                        mois = "11"

                    else:
                        mois = "12"

                    ANNONCE_DATE = annee+"-"+mois+"-"+jour

        except:
            pass
        TYPE = ANNONCE_LINK.split("/")[-1]
        if TYPE.find('vente') != -1:
            ACHAT_LOC = "1"
        elif TYPE.find('location') != -1:
            ACHAT_LOC = "2"
        else:
            ACHAT_LOC = ""

        SOLD = "N"
        MAISON_APT = ""

        NEUF_IND = ""
        try:
            NOM = soup.find(
                "h1", {"class": "serif-light title-property"}).get_text()
            for i in NOM:
                if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                    NOM = NOM.replace(i, " ")
        except:
            pass

        try:
            CATEGORIE = ANNONCE_LINK.split("-")[1]

        except:
            pass
        if CATEGORIE == "propriete":
            CATEGORIE = "maison"

        ADRESSE = ""
        CP = ""

        try:
            VILLE = soup.findAll(
                'span', {'class': 'breadcrumb-name'})[4].get_text()
        except:
            pass
        QUARTIER = ""
        try:
            DEPARTEMENT = soup.findAll(
                'span', {'class': 'breadcrumb-name'})[3].get_text().split("-")[-2]

        except:
            pass
        try:
            REGION = soup.findAll(
                'span', {'class': 'breadcrumb-name'})[2].get_text().split("-")[0:-1]
        except:
            pass
        PROVINCE = ""
        try:
            ANNONCE_TEXT = soup.find(
                'span', {'data-role': 'description-text-content'}).get_text()
            for i in ANNONCE_TEXT:
                if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                    ANNONCE_TEXT = ANNONCE_TEXT.replace(i, " ")
                    ANNONCE_TEXT = ANNONCE_TEXT.strip(" ")

        except:
            pass

        ETAGE = ""
        LATITUDE = ""
        LONGITUDE = ""

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Nombre Étages":
                    NB_ETAGE = i.find(
                        "div", {"class": "single-value"}).get_text()
                    for i in NB_ETAGE:
                        if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                            NB_ETAGE = NB_ETAGE.replace(i, " ")

        except:
            pass

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Superficie interne":
                    M2_TOTALE = i.find(
                        "div", {"class": "single-value"}).get_text()
                    for i in M2_TOTALE:
                        if i.isdigit() == False:
                            M2_TOTALE = M2_TOTALE.replace(i, "")
                    M2_TOTALE = M2_TOTALE.replace(M2_TOTALE[-1], "")
                    M2_TOTALE = M2_TOTALE.strip(" ")

        except:
            pass

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Superficie externe":
                    SURFACE_TERRAIN = i.find(
                        "div", {"class": "single-value"}).get_text()
                    for i in SURFACE_TERRAIN:
                        if i.isdigit() == False:
                            SURFACE_TERRAIN = SURFACE_TERRAIN.replace(i, "")
                    SURFACE_TERRAIN = SURFACE_TERRAIN.replace(
                        SURFACE_TERRAIN[-1], "")
                    SURFACE_TERRAIN = SURFACE_TERRAIN.strip(" ")

        except:
            pass

        NB_GARAGE = ""

        try:
            PHOTO = soup.find(
                "div", {"class": "img-box__content"}).find("span").get_text()
        except:
            pass

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Pièces":
                    PIECE = i.find("div", {"class": "single-value"}).get_text()
                    for i in PIECE:
                        if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                            PIECE = PIECE.replace(i, " ")
        except:
            pass

        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Chambres":
                    NB_CHAMBRE = i.find(
                        "div", {"class": "single-value"}).get_text()
                    for i in NB_CHAMBRE:
                        if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                            NB_CHAMBRE = NB_CHAMBRE.replace(i, " ")

        except:
            pass

        P_TEST = ""
        try:
            for i in features:
                if i.find('span', {'class': 'feat-label'}).get_text() == "Services Extérieurs":
                    P_TEST = i.find(
                        "div", {"class": "multiple-values"}).get_text()
        except:
            pass

        if "Piscine" in P_TEST:
            PISCINE = "Y"
        else:
            PISCINE = "N"

        try:
            PRIX = soup.find("div", {"data-role": "property-price"}).get_text()
        except:
            pass
        try:
            for i in PRIX:
                if i.isdigit() == False:
                    PRIX = PRIX.replace(i, "")
            PRIX = PRIX.strip(" ")
            PRIX = PRIX.replace(" ", "")
        except:
            pass

        PRIX_M2 = ""
        URL_PROMO = ""
        STOCK_NEUF = ""

        # PAYS_AD="FR"
        try:
            PAYS_AD = soup.findAll(
                'span', {'class': 'breadcrumb-name'})[1].get_text()
        except:
            pass

        PRO_IND = ""
        SELLER_TYPE = "pro"
        MINI_SITE_URL = ""
        MINI_SITE_ID = ""

        try:
            AGENCE_NOM = soup.find(
                "div", {"class": "agency__name-container"}).find("a").get_text()
            for i in AGENCE_NOM:
                if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                    AGENCE_NOM = AGENCE_NOM.replace(i, " ")
        except:
            pass

        try:
            AGENCE_ADRESSE = soup.find(
                "div", {"class": "agency__location-container small text-muted address"}).get_text()
            for i in AGENCE_ADRESSE:
                if i in [",", ".", ";", "\n", "\t", "\a", "\b", "\r"]:
                    AGENCE_ADRESSE = AGENCE_ADRESSE.replace(i, " ")
        except:
            pass

        AGENCE_CP = ""

        if len(AGENCE_ADRESSE.split(" -")) == 2:
            AGENCE_VILLE = AGENCE_ADRESSE.split(" -")[0]
            AGENCE_VILLE = AGENCE_VILLE.replace(",", "-")

        if len(AGENCE_ADRESSE.split(" -")) == 2:
            AGENCE_DEPARTEMENT = AGENCE_ADRESSE.split(" -")[1]
            AGENCE_DEPARTEMENT = AGENCE_DEPARTEMENT.replace(",", "-")

        EMAIL = ""
        WEBSITE = ""
        AGENCE_TEL0 = ""
        try:
            att = soup.findAll("div", {
                               "class": "agency__contact agency__contact-phone condensed-bold"})[0].find("a").attrs
            AGENCE_TEL0 = att['data-track-phone-value']
        except:
            pass
        i = len(AGENCE_TEL0) - 1
        while i >= 0:
            AGENCE_TEL += AGENCE_TEL0[i]
            i -= 1

        for i in AGENCE_TEL:
            if i == " ":
                AGENCE_TEL = AGENCE_TEL.replace(i, "")

        AGENCE_TEL = AGENCE_TEL.replace("+33", "")
        AGENCE_TEL = AGENCE_TEL.replace("0033", "")
        AGENCE_TEL = AGENCE_TEL.replace("+44", "")
        AGENCE_TEL = AGENCE_TEL.replace("+49", "")
        AGENCE_TEL = AGENCE_TEL.replace("+", "")
        AGENCE_TEL = AGENCE_TEL.replace("(0)", "")

        AGENCE_TEL_2 = ""
        AGENCE_TEL_3 = ""
        AGENCE_TEL_4 = ""
        AGENCE_FAX = ""
        AGENCE_CONTACT = ""
        PAYS_DEALER = ""
        FLUX = ""
        SIREN = ""

        itm["ANNONCE_LINK"] = ANNONCE_LINK
        itm["FROM_SITE"] = FROM_SITE
        itm["ID_CLIENT"] = ID_CLIENT
        itm["ANNONCE_DATE"] = ANNONCE_DATE
        itm["ACHAT_LOC"] = ACHAT_LOC
        itm["SOLD"] = SOLD
        itm["MAISON_APT"] = MAISON_APT
        itm["CATEGORIE"] = CATEGORIE
        itm["NEUF_IND"] = NEUF_IND
        itm["NOM"] = NOM
        itm["ADRESSE"] = ADRESSE
        itm["CP"] = CP
        itm["VILLE"] = VILLE
        itm["QUARTIER"] = QUARTIER
        itm["DEPARTEMENT"] = DEPARTEMENT
        itm["REGION"] = REGION
        itm["PROVINCE"] = PROVINCE
        itm["ANNONCE_TEXT"] = ANNONCE_TEXT
        itm["ETAGE"] = ETAGE
        itm["NB_ETAGE"] = NB_ETAGE
        itm["LATITUDE"] = LATITUDE
        itm["LONGITUDE"] = LONGITUDE
        itm["M2_TOTALE"] = M2_TOTALE
        itm["SURFACE_TERRAIN"] = SURFACE_TERRAIN
        itm["NB_GARAGE"] = NB_GARAGE
        itm["PHOTO"] = PHOTO
        itm["PIECE"] = PIECE
        itm["NB_CHAMBRE"] = NB_CHAMBRE
        itm["PISCINE"] = PISCINE
        itm["PRIX"] = PRIX
        itm["PRIX_M2"] = PRIX_M2
        itm["URL_PROMO"] = URL_PROMO
        itm["STOCK_NEUF"] = STOCK_NEUF
        itm["PAYS_AD"] = PAYS_AD
        itm["PRO_IND"] = PRO_IND
        itm["SELLER_TYPE"] = SELLER_TYPE
        itm["MINI_SITE_URL"] = MINI_SITE_URL
        itm["MINI_SITE_ID"] = MINI_SITE_ID
        itm["AGENCE_NOM"] = AGENCE_NOM
        itm["AGENCE_ADRESSE"] = AGENCE_ADRESSE
        itm["AGENCE_CP"] = AGENCE_CP
        itm["AGENCE_VILLE"] = AGENCE_VILLE
        itm["AGENCE_DEPARTEMENT"] = AGENCE_DEPARTEMENT
        itm["EMAIL"] = EMAIL
        itm["WEBSITE"] = WEBSITE
        itm["AGENCE_TEL"] = AGENCE_TEL
        itm["AGENCE_TEL_2"] = AGENCE_TEL_2
        itm["AGENCE_TEL_3"] = AGENCE_TEL_3
        itm["AGENCE_TEL_4"] = AGENCE_TEL_4
        itm["AGENCE_FAX"] = AGENCE_FAX
        itm["AGENCE_CONTACT"] = AGENCE_CONTACT
        itm["PAYS_DEALER"] = PAYS_DEALER
        itm["FLUX"] = FLUX
        itm["SIREN"] = SIREN

        yield itm
