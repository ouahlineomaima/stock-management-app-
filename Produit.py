import mysql.connector

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
        while cursor.fetchone() is not None:
            id, nom, quantite, _, prix, mini, maxi = cursor.fetchone()
            produit = Produit(id, nom, int(quantite), int(mini), int(maxi), service, int(prix))
            list_produit.append(produit)
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
        self.iD = iD
        self.nom = nom
        self.quantite = quantite
        if not min:
            self.min = 0
        else:
            self.min = min
        if not max:
            self.max = max
        else:
            self.max = max
        self.service = service
        self.prix = prix

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
