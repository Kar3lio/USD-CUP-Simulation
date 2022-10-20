import configparser
import statistics as stats
from matplotlib import scale
from scipy.stats import skewnorm
import matplotlib.pyplot as plt

# region Reading all settings
config = configparser.ConfigParser()
config.read('config.ini')

mct = config['DEFAULT']['MEASURE_OF_CENTRAL_TENDENCY']
if mct not in ['median', 'mode', 'mean']:
    raise Exception(
        'Incorrect configuration of the measures of central tendency')
number_of_ads = int(config['DEFAULT']['NUMBER_OF_DAYLI_ADS'])
days = int(config['DEFAULT']['NUMBER_OF_DAYS'])
# endregion


def read_script_value(path_file):
    """
    Read all data stored in the script
    """
    try:
        file = open(path_file)
        values = list(map(float, file.read().split('\n')))
        return values
    finally:
        file.close()


values = read_script_value('db.txt')
current_value = values[0]
skewness = int(config['RANDOM_VARIANLE']['SKEWNESS'])  #Negative values are left skewed, positive values are right skewed.
standard = int(config['RANDOM_VARIANLE']['SCALE'])     #Standard desviation

for i in range(days):
    random = skewnorm.rvs(a = skewness, loc=current_value, scale = standard, size = number_of_ads)  #Skewnorm function
    if mct=="median":
        current_value = stats.median(random)
    elif mct=="mode":
        current_value = stats.mode(random)           
    else:
        current_value = stats.mean(random)
    print(current_value)
