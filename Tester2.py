import matplotlib.pyplot as plt

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

values = read_script_value('values.txt')
plt.hist(values,15)
plt.show()