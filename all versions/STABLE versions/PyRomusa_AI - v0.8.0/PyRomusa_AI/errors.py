"""
Aici se vor crea erori Python personalizate pentru PyRomusa AI
"""
# SameNotAllowedError:
    #   Vei da de această eroare când două variabile au aceeași valoare, 
    # și ele, în mod normal, nu ar trebui să aibe aceleași valori în același timp


class SameNotAllowedError(Exception):
    pass

    
    