import mysql.connector
from PyQt5.QtWidgets import *

# test commit and push


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


def get_allproduit(service):
    list_produit = []
    try:
        cursor, db = get_connection()
        request = f"SELECT * FROM produit WHERE service = {service.iD}"
        cursor.execute(request)
        row = cursor.fetchone()
        while row is not None:
            id, nom, quantite, _, prix, mini, maxi = row
            produit = Produit(id, nom, int(quantite), int(mini), int(maxi), service, int(prix))
            list_produit.append(produit)
            row = cursor.fetchone()
        return list_produit
    except mysql.connector.Error:
        return list_produit


def get_produit(id_produit, service):
    for produit in get_allproduit(service):
        if produit.iD == id_produit:
            return produit
    return None


class Produit:

    def __init__(self, iD, nom, quantite, min, max, service, prix):
        try:
            self.iD = iD
            self.nom = nom
            self.quantite = int(quantite)
            if not min:
                self.min = 0
            else:
                self.min = int(min)
            if not max:
                self.max = 100
            else:
                self.max = int(max)
            self.service = service
            try:
                self.prix = float(prix)
            except TypeError as e:
                print(e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Valeur de prix non rèelle. Veuillez saisir une valeur rèelle.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        except BaseException as e:
            print(e)

    def set_service(self, service):
        try:
            self.service = service
            cursor, db = get_connection()
            cursor.execute(f"UPDATE `gestionstock`.`produit` SET `service` = '{service.iD}' WHERE (`idproduit` = '{self.iD}');")
            db.commit()
        except mysql.connector.Error as e:
            print(e.msg)

    def achat_produit(self, quantite):
        product = get_produit(self.iD[6:])
        product.quantite -= quantite
        cursor, db = get_connection()
        cursor.execute(f"update produit set quantite = {product.quantite} where idproduit = {product.iD}")

    def __str__(self):
        return self.nom

    def __eq__(self, other):
        if isinstance(other, Produit):
            return self.iD == other.iD and self.nom == other.nom and self.quantite == other.quantite and self.min == other.min and self.max == other.max and self.service.iD == other.service.iD and self.prix == other.prix
        return False
