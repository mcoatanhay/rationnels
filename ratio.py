#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: rationnels.py
# Auteur: Marc COATANHAY

"""
    Module python pour effectuer des calculs rationnels.

"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
import entiers.ent as entier

# Définitions constantes et variables globales

# Définitions fonctions et classes
class Rationnel():
    """Classe permettant d'effectuer des opérations sur des rationnels."""
    def __init__(self,num=1,den=1):
        """Initialise un élément de class Rationnel"""
        self.num = int(num)
        self.den = int(den)
        pgcd = entier.pgcd(self.num,self.den)
        if(pgcd != 0):
            self.num = self.num//pgcd
            self.den = self.den//pgcd

    def __repr__(self):
        """Affichage d'un terme Rationnel"""
        chaine = ''
        chaine += str(self.num)
        chaine += '/'
        chaine += str(self.den)
        return chaine

    def __add__(r1,r2):
        """Additionne deux termes Rationnels"""
        if(r1.den != r2.den):
            num = r1.num*r2.den + r2.num*r1.den
            den = r1.den*r2.den
        else:
            num = r1.num + r2.num
            den = r1.den
        pgcd = entier.pgcd(num,den)
        if(den < 0):
            den = abs(den)
            num = - num
        if(pgcd != 0):
            num = num//pgcd
            den = den//pgcd
        return Rationnel(num,den)
        return chaine

    def __mul__(r1,r2):
        """Multiplie deux termes Rationnels"""
        num = r1.num*r2.num
        den = r1.den*r2.den
        pgcd = entier.pgcd(num,den)
        if(pgcd != 0):
            num = num//pgcd
            den = den//pgcd
        return Rationnel(num,den)

    def __neg__(self):
        """Calcule l'opposé d'un terme Rationnel"""
        return Rationnel(-self.num,self.den)

    def __sub__(r1,r2):
        """Soustrait deux termes Rationnels"""
        return r1 + (- r2)

    def __truediv__(r1,r2):
        """Divise deux termes Rationnels"""
        num = r1.num*r2.den
        den = r1.den*r2.num
        pgcd = entier.pgcd(num,den)
        if(pgcd != 0):
            num = num//pgcd
            den = den//pgcd
        return Rationnel(num,den)



print("* Module : rationnels /ok")