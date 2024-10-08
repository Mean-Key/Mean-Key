import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'):  
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':

    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(midterm_kr, final_kr, color='red', label='Korean')
    plt.scatter(midterm_en, final_en, color='blue', marker='+', label='English')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.grid(True)
    plt.legend(loc=2)

    plt.subplot(1, 2, 2)
    plt.hist(total_kr, bins=range(0, 105, 5), alpha=0.5, color='red', label='Korean')
    plt.hist(total_en, bins=range(0, 105, 5), alpha=0.5, color='cornflowerblue', label='English')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.xlim([0, 100])
    plt.legend(loc=2)

    plt.tight_layout()
    plt.show()