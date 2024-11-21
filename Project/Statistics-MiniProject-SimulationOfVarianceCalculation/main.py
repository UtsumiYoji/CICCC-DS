import numpy

def main():
    # Settings
    POPULATION_NUM = 1000000
    SAMPLE_NUMS = [100, 1000, 10000, 100000]

    # Generate random data
    random_generater = numpy.random.default_rng()
    random_data = random_generater.random(POPULATION_NUM)

    # Print header
    print('', 'Mean', "Var", "Std", sep='\t\t\t')

    # Print population data
    print('Population\t', numpy.mean(random_data), numpy.var(random_data), numpy.std(random_data), sep='\t')

    # Print sample data
    for sample_num in SAMPLE_NUMS:
        sample_data = random_generater.choice(random_data, sample_num)
        for ddof in range(2):
            print('sample-'+str(sample_num)+'-ddof-'+str(ddof), numpy.mean(sample_data), numpy.var(sample_data, ddof=ddof), numpy.std(sample_data, ddof=ddof), sep='\t')

if __name__ == "__main__":
    main()