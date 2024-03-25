import pandas as pd

def resume_table(df: pd.DataFrame, index: bool = False) -> pd.DataFrame:
    """
    Give an overview of a dataframe

    df : pd.DataFrame 
        Dataframe to process
    
    index : bool, default False
        True: indlude the index in the overview
        False: doesn't include the index in the overview

    returns: pd.DataFrame
    """

    print("Dataframe shape : {}".format(df.shape))

    # Get list of columns names in the dataframe
    list_columns = df.columns

    # Declare the columns for the returned dataframe
    cols = ["type","nb_nan","nb_unique","v1","v2","v3"]

    # Declare an empty list that will recieve data for the returned dataframe
    list_data = []
    
    # Iterate over the dataframe columns names
    for i in list_columns :
        # Get current dataframe column
        x = df[i]

        # Append to the list of data: value type, number of NA values, number of unique values and the 3 first values
        list_data.append([x.dtypes,x.isna().sum(),x.nunique(),x.iloc[0], x.iloc[1], x.iloc[2]])

    # Check if we add the index to the overview
    if index:

        # Get index
        x = df.index

        # Insert to the first position of the list of data: value type, number of NA values, number of unique values and the 3 first values
        list_data.insert(0,[x.dtype,x.isna().sum(),x.nunique(),x[0], x[1], x[2]])

        # Insery index name in first position of the column names list
        list_columns = list_columns.insert(0,x.name)
    
    # Convert the list to a dataframe and return it
    df_return = pd.DataFrame(list_data, columns=cols, index=list_columns)

    return(df_return)

def get_changes(serie: pd.Series) -> pd.Series:
    """
    Categorize evolution of values with a serie of integers incrementing when the value of the serie is changing.

    serie : pd.Series 
        Serie to process

    returns : pd.Series
    """

    # Compare if each value is different from the previous one and do the cumulative sum of it
    serie_evolution = (serie != serie.shift()).cumsum()

    return serie_evolution