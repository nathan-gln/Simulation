import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
#le but de la simulation est simple, considerons une piece avec plusieurs plat avec deux de nourritures dedans que nous representerons par une liste vide de taille n avec n le nombre de nourriture/2 et deux equipes l'equipe bleu et rouge, ensuite je repartie aleatoirement les membres  de chaque aquipe devant chaque plat sachant qu'il ne peut avoir que deux personnes devant un plat, ensuite j'applique certaines conditions qui font evoluer le nombre de membres dans les equipes et je represente l'evolutions des deux equipes.





#pour la premiere simulation il n'y a que une equipe, l'equipe bleu, et les conditions sont que si un membres de l'equipe est seul devant un plat il se reproduit et si il y en a deux alors les deux survient mais ne se reproduit pas et stagne a n*2


def simulation_1(equipe,n,etape):
    L1 = []
    def simulation_a(equipe,n,etape):
        if etape == 0:
                return L1
        else:
            if equipe >= n*2:
                L1.append(n*2)
                return simulation_a(equipe,n,etape-1)
            L1.append(equipe)
            L = [0 for _ in range(n)]
            for _ in range(0,equipe):
                x = rd.randint(0,len(L))    #pas sur des ces trois
                while L[x] == 3:            #lignes de code
                    x = rd.randint(0,len(L))#qui on pour but d'empecher d'avoir trois membres
                L[x] += 1
        for elt in L:
            if elt == 1:
                equipe += 1
        return simulation_a(equipe,n,etape-1)
    simulation_a(equipe,n,etape)
    return L1


#pour cette simulation il y a les deux equipes, les conditions de l'equipe bleu restent les memes et les nouvelles sont que si il y a un membre de l'equipe bleu et de l'equipe rouge au meme plat alors le bleu a 1 chance sur 2 de survivre et le rouge 1 chance sur 2 de se reproduire et si il y a deux membres de l'equipe rouge a un plat les deux meurent

def simulation_2(e1, e2, n, etape):
    L1 = []
    L2 = []
    def simulation_b(e1, e2, n, etape):
        if etape == 0:
            return L1, L2
        else:
            L1.append(e1)
            L2.append(e2)
            for _ in range(n):
                L = [[] for _ in range(n)]
                mort = []
                for _ in range(e1):
                    x = rd.randint(0, n - 1)
                    if len(L[x]) >= 2:
                        count1 = 0
                        while len(L[x]) >= 2:
                            x = rd.randint(0, n - 1)
                            count1 += 1
                            if count1 > 1000:
                                mort.append('bleu')
                                break
                    L[x].append('bleu')
                for _ in range(e2):
                    x = rd.randint(0, n - 1)
                    if len(L[x]) >= 2:
                        count2 = 0
                        while len(L[x]) >= 2:
                            x = rd.randint(0, n - 1)
                            count2 += 1
                            if count2 > 1000:
                                mort.append('rouge')
                                break
                    L[x].append('rouge')
                E1, E2 = repro_dead(L, mort, e1, e2)
            return simulation_b(E1, E2, n, etape - 1)
    return simulation_b(e1, e2, n, etape)


# celle ci est la meme que simulation_2 sauf que la il a differentes possibilies de choix (je vous ai aussi envoie une note avec un tableau avec les proba)
def simulation_3(e1,e2,n,etape):
    L1 = []
    L2 = []

    def simulation_c(e1, e2, n, etape):
        if etape == 0:
            return L1, L2
        else:
            L1.append(e1)
            L2.append(e2)
            for _ in range(n):
                L = [[] for _ in range(n)]
                mort = []
                for _ in range(e1):
                    x = rd.randint(0, n - 1)
                    if len(L[x]) >= 2:
                        count1 = 0
                        while len(L[x]) >= 2:
                            x = rd.randint(0, n - 1)
                            count1 += 1
                            if count1 > 1000:
                                mort.append('bleu')
                                break
                    L[x].append('bleu')
                for _ in range(e2):
                    x = rd.randint(0, n - 1)
                    if len(L[x]) >= 2:
                        count2 = 0
                        while len(L[x]) >= 2:
                            x = rd.randint(0, n - 1)
                            count2 += 1
                            if count2 > 1000:
                                mort.append('rouge')
                                break
                    L[x].append('rouge')
                E1, E2 = repro_dead_avec_choix(L, mort, e1, e2)
            return simulation_c(E1, E2, n, etape - 1)
    return simulation_c(e1, e2, n, etape)

def repro_dead_avec_choix(L,mort,e1,e2):
    for elt in L:
        if elt == ['bleu','bleu']:
            if survie_choix(1/10) == 1:
                e1 += survie_choix(1/2)
                e1 -= survie_choix(1/2)
        elif elt == ['rouge']:
            e2 += 1
        elif elt == ['bleu']:
            e1 += 1
        elif elt == ['bleu', 'rouge']:   #code pour simulation_3
            if survie_choix(8/10) == 1:
                e1 -= survie_choix(1/2)
                e2 += survie_choix(1/2)
        elif elt == ['rouge', 'rouge']:
            if survie_choix(1/2) == 1:
                e2 -= 2
            else:
                e2 -= 2*survie_choix(1/4)
    for elt in mort:
        if elt == 'bleu':
            e1 -= 1
        elif elt == 'rouge':
            e2 -= 1
    return e1, e2

def repro_dead(L, mort, e1, e2):
    for elt in L:
        if elt == ['bleu']:
            e1 += 1
        elif elt == ['rouge']:
            e2 += 1
        elif elt == ['bleu', 'rouge']:   #code pour simulation_2
            e1 -= survie_choix(1/2)
            e2 += survie_choix(1/2)
        elif elt == ['rouge', 'rouge']:
            e2 -= 2
    for elt in mort:
        if elt == 'bleu':
            e1 -= 1
        elif elt == 'rouge':
            e2 -= 1
    return e1, e2

def survie_choix(p):
    if rd.random() < p:
        return 1
    return 0

def voir_sim_1(L):
    plt.plot(L,'-')
    plt.show()

def voir_sim_2_3(L):
    L1,L2 = L
    plt.plot(L1,'-')
    plt.plot(L2,'-')
    plt.show()