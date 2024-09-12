import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

def two_proportion_test(successes1, n1, successes2, n2, tail, significance_level=0.05):
    p1 = successes1 / n1
    p2 = successes2 / n2
    p = (successes1 + successes2) / (n1 + n2)
    z = (p1 - p2) / np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    
    if tail == 'left':
        p_value = stats.norm.cdf(z)
    elif tail == 'right':
        p_value = 1 - stats.norm.cdf(z)
    elif tail == 'both':
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z)))
    
    print('p-value:', p_value)
    if p_value < significance_level:
        print("The null hypothesis can be rejected.")
    else:
        print("The null hypothesis cannot be rejected.")

def main():
    data = pd.read_csv('ab_data.csv')
    data.dropna(inplace=True)
    data['day'] = pd.to_datetime(data['timestamp']).dt.day
    data['hour'] = pd.to_datetime(data['timestamp']).dt.hour

    print('\n----------------------Part1----------------------\n')

    data_a = data[data['group'] == 'control']
    data_b = data[data['group'] == 'treatment']

    print('control\n', data_a['converted'].describe(), '\n', sep='')
    print('treatment\n', data_b['converted'].describe(), sep='')

    print('\n----------------------Part2----------------------\n')

    print('Null hypothesis: The new landing page has no effect on conversion')
    print('Alternative hypothesis: The new landing page increases conversion rates.')

    sns.barplot(data=data, x='group', y='converted')
    plt.show()

    print('\n----------------------Part3----------------------\n')

    two_proportion_test(
        data_a['converted'].sum(), len(data_a), 
        data_b['converted'].sum(), len(data_b),
        'right'
    )

    print('\n----------------------Part4----------------------\n')

    print(stats.t.interval(
        0.95, 
        len(data_a['converted']) - 1, 
        loc=np.mean(data_a['converted']), 
        scale=stats.sem(data_a['converted'])
        ))
    
    print(stats.t.interval(
        0.95, 
        len(data_b['converted']) - 1, 
        loc=np.mean(data_b['converted']), 
        scale=stats.sem(data_b['converted'])
        ))
    
    print("both data outputed low number, it means landing_page doesn't matter to be converted")

    print('\n----------------------Part5----------------------\n')

    sns.lineplot(data=data, x='day', y='converted', hue='group')
    plt.show()

    print('On 10th day, the control group has higher conversion rate more than usual.')
    print('On the other hand, the treatment group has lower conversion rate more than usual.')

    print('\n----------------------Part6----------------------\n')

    print('As two proportion test, the new landing page has no effect on conversion.')
    print('But, the control group has higher conversion rate on 10th day.')
    print('So it is worth to look into the data more.')

if __name__ == '__main__':
    main()