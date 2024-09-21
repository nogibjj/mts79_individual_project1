from main import generate_full_summary, generate_column_report
import seaborn as sns
import pandas as pd

dataset = sns.load_dataset('diamonds')


def test_generate_full_summary():
    """
    Test if generate_full_summary function returns the correct keys and values.
    """
    result = generate_full_summary(dataset)

    # Check if the result contains the correct keys
    assert "Summary Statistics" in result
    assert "Mode" in result
    assert "Variance and Standard Deviation" in result
    
    # Check the types of the values
    assert isinstance(result["Summary Statistics"], pd.DataFrame)
    assert isinstance(result["Mode"], pd.Series)
    assert isinstance(result["Variance and Standard Deviation"], dict)


def test_generate_column_report():
    """
    Test if generate_column_report function returns the correct summary for a specific column.
    """
    result = generate_column_report(dataset, 'price')

    # Check if the result contains the correct keys
    assert "Summary Statistics" in result
    assert "Mode" in result
    assert "Variance" in result
    assert "Standard Deviation" in result
    
    # Check the types of the values
    assert isinstance(result["Summary Statistics"], pd.DataFrame)
    assert isinstance(result["Mode"], (int, float))
    assert isinstance(result["Variance"], float)
    assert isinstance(result["Standard Deviation"], float)


if __name__ == '__main__':
    test_generate_full_summary()
    test_generate_column_report()