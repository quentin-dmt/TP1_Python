import numpy as np
def simulation(nombre) :
    resultat = []
    for x in range(nombre) :
        proba = 32455859./(32455859.+34534967.)
        echantillon = np.random.binomial(1,proba,100)
        n = len([nb for nb in echantillon if nb == 1])
        hommes = np.random.normal(77.4, np.sqrt(12.), n)
        femmes = np.random.normal(62.4, np.sqrt(10.9), 100-n)
        poids = np.concatenate([hommes, femmes])
        poids_final = np.sum(poids)
        if poids_final < 7200.:
            resultat.append(0.)
        else :
            resultat.append(1.)
    return (np.sum(resultat)/nombre)

print(simulation(1000))