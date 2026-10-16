import DataPreprocessing
import DataModeling

def main():
    DataPreprocessing.collect_data()
    DataPreprocessing.prepare_data()
    DataPreprocessing.exploratory_data_analysis()

    DataModeling.calc_corr()
    DataModeling.visualize()

if __name__ == '__main__':
    main()

    
