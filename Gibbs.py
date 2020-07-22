import pandas as pd

Gibbs_data = pd.read_csv('Gibbs_free_energy.csv')


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("-------------------")
        print(round(func(*args, **kwargs), 2), 'kJ/mol')
        print("-------------------", '\n')
    return wrapper

@my_decorator
def calculate_Gibbs_298K(Reaction, name):
    '''
    Calculates the Gibbs free energy at 298 K of reaction from the data available
    in Gibbs_free_energy.csv data
    Arguments:
    - Reaction: Python dictionary with key as compounds and values as stoichimetry
    coefficient (Remember to put negative to reactants)

    Returns:
    The value of the Gibbs free energy at 298 K
    '''
    print(name)
    return sum([Gibbs_data[Gibbs_data['formula'] == key]['Delta Gf 298 K (kJ/mol)'].values[0] 
    * value for key,value in Reaction.items()])





calculate_Gibbs_298K({'NH3':-4, 'NO':-4, 'O2':-1, 'N2':4, 'H2O':6}, 'Standard SCR')

calculate_Gibbs_298K({'NH3':-4, 'NO':-2, 'NO2':-2, 'N2':4, 'H2O':6}, 'Fast SCR')

calculate_Gibbs_298K({'NH3':-8, 'NO2':-6, 'N2':7, 'H2O':12}, 'Slow SCR')

calculate_Gibbs_298K({'NH3':-4, 'O2':-5, 'NO':4, 'H2O':6}, 'Ammonia oxidation')

calculate_Gibbs_298K({'NO':-2, 'O2':-1, 'NO2':2}, 'NO oxidation')
