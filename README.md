# Description

Ce projet est un petit outil de scan réseau réalisé en Python. Il permet de vérifier rapidement certains éléments de sécurité d'un site web ou d'un serveur.

## Fonctionnalités

* Demande à l'utilisateur le nom de domaine à analyser.
* Vérifie si les ports courants **22 (SSH)**, **80 (HTTP)** et **443 (HTTPS)** sont ouverts ou fermés.
* Teste si le site est accessible en **HTTPS**.
* Recherche la présence d'une page d'administration (`/admin`).
* Affiche les résultats du scan directement dans le terminal.

## Objectif

Ce script a été conçu dans un but d'apprentissage afin de découvrir les bases du scan réseau et de l'analyse simple d'un site web avec Python. Il ne remplace pas des outils professionnels de sécurité, mais permet de comprendre le fonctionnement des connexions réseau, des requêtes HTTP et de la détection de services.

