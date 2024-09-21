def get_summary_statistics(df):
    return df.describe()

def get_mode(df):
    return df.mode().iloc[0]

def get_variance_std(df, col):
    variance = df[col].var()
    std_dev = df[col].std()
    return variance, std_dev