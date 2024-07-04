from nada_dsl import *
import numpy as np
from scipy.stats import linregress, ttest_ind

def complex_analysis():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    party5 = Party(name="Party5")
    
    # Generate random data for each party
    data_size = 100
    data_party1 = np.random.normal(loc=10, scale=2, size=data_size)
    data_party2 = np.random.normal(loc=8, scale=3, size=data_size)
    data_party3 = np.random.normal(loc=12, scale=1.5, size=data_size)
    data_party4 = np.random.uniform(low=5, high=15, size=data_size)
    data_party5 = np.random.chisquare(df=3, size=data_size)
    
    # Define secret inputs as arrays
    input_party1 = SecretArray(Input(name="Data1", party=party1, data=data_party1.tolist()))
    input_party2 = SecretArray(Input(name="Data2", party=party2, data=data_party2.tolist()))
    input_party3 = SecretArray(Input(name="Data3", party=party3, data=data_party3.tolist()))
    input_party4 = SecretArray(Input(name="Data4", party=party4, data=data_party4.tolist()))
    input_party5 = SecretArray(Input(name="Data5", party=party5, data=data_party5.tolist()))
    
    # Perform computations
    # Descriptive statistics
    mean1 = np.mean(data_party1)
    mean2 = np.mean(data_party2)
    mean3 = np.mean(data_party3)
    std_dev4 = np.std(data_party4)
    var5 = np.var(data_party5)
    
    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(data_party1, data_party2)
    
    # Hypothesis testing
    _, t_pvalue = ttest_ind(data_party3, data_party4)
    
    # Outputs
    output1 = Output(mean1, "mean_data1_output", party1)
    output2 = Output(mean2, "mean_data2_output", party2)
    output3 = Output(mean3, "mean_data3_output", party3)
    output4 = Output(std_dev4, "std_dev_data4_output", party4)
    output5 = Output(var5, "variance_data5_output", party5)
    
    output6 = Output(slope, "slope_data1_data2_output", party1)
    output7 = Output(intercept, "intercept_data1_data2_output", party2)
    output8 = Output(r_value, "r_value_data1_data2_output", party3)
    output9 = Output(p_value, "p_value_data1_data2_output", party4)
    output10 = Output(std_err, "std_err_data1_data2_output", party5)
    
    output11 = Output(t_pvalue, "ttest_pvalue_data3_data4_output", party1)
    
    # Return outputs
    return [output1, output2, output3, output4, output5, output6, output7, output8, output9, output10, output11]

# Example usage
if __name__ == "__main__":
    results = complex_analysis()
    for result in results:
        print(f"Output for {result.party.name}: {result.value}")
