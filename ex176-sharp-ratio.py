import numpy as np

returns = [0.05, 0.1, 0.15, -0.03, 0.12]
risk_free_rate = 0.02

import numpy as np

def sharpe_ratio(returns, risk_free_rate):
    returns = np.array(returns)
    excess_return = returns - risk_free_rate
    mean_excess_return = np.mean(excess_return)
    std_dev = np.std(returns, ddof=0)  # population standard deviation
    sharpe = mean_excess_return / std_dev
    return sharpe

ratio = sharpe_ratio(returns, risk_free_rate)
print(f"Sharpe Ratio: {ratio}")
