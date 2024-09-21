from main import (generate_full_summary, generate_column_report)
import seaborn as sns
import pandas as pd
dataset = sns.load_dataset('diamonds')

def test_generate_full_summary():
    """
    Test if generate_full_summary function returns the correct keys and values.
    """
    result = generate_full_summary(dataset)
    result.assertIn("Summary Statistics", result)
    result.assertIn("Mode", result)
    result.assertIn("Variance and Standard Deviation", result)
    result.assertIsInstance(result["Summary Statistics"], pd.DataFrame)

def test_generate_column_report():
    """
    Test if generate_column_report function returns the correct summary for a specific column.
    """
        
    result = generate_column_report(dataset, 'price')
    result.assertIn("Summary Statistics", result)
    result.assertIn("Mode", result)
    result.assertIn("Variance", result)
    result.assertIn("Standard Deviation", result)

if __name__ == '__main__':
    test_generate_full_summary()
    test_generate_column_report()