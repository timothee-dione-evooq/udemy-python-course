from scipy.optimize import root_scalar

def internal_rate_of_return(cashflows):
    def npv(r):
        return sum(cf / (1 + r)**i for i, cf in enumerate(cashflows))

    # Cherche une racine dans l'intervalle [0, 1]
    result = root_scalar(npv, bracket=[-0.9999, 1], method='brentq')

    if result.converged:
        return result.root
    else:
        raise ValueError("Le calcul du TRI n'a pas convergé.")

# Exemple d'utilisation
cashflows = [-5000, 2000, 3000, 4000]
tri = internal_rate_of_return(cashflows)
print(f"Le TRI est : {tri:.4%}")
