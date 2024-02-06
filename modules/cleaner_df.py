# Import the numpy and pandas modules
import numpy as np
import pandas as pd
# Import the get_logger function from the app_loggs module
from app_loggs import get_logger

# Create a logger object with the name "DfCleaner"
my_logger = get_logger("DfCleaner")
# Log a debug message that the cleaning module is loaded successfully
my_logger.debug("Cleaning Module Loaded successfully!")

# Define a class to clean pandas data frames
class DfCleaner():
    """
        This class has functions for cleaning pandas data frames by removing duplicates,
        dropping columns or rows and more.
    """

    # Initialize the class
    def __init__(self):
        pass

    # Define a method to convert a list of labels to lowercase separated by underscore
    def fixLabel(self, label: list) -> list:
        """This method takes a list of labels and returns a list of labels in lower case, separated by underscore

        Args:
            label (list): a list of labels

        Returns:
            list: a list of labels in lower case, separated by underscore
        """
        # Strip any leading or trailing spaces from the label
        label = label.strip()
        # Replace any spaces, dots, or slashes with underscores
        label = label.replace(' ', '_').replace('.', '').replace('/', '_')
        # Return the label in lower case
        return label.lower()

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """drop duplicate rows

        Args:
            df (pd.DataFrame): pandas data frame

        Returns:
            pd.DataFrame: pandas data frame
        """
        df.drop_duplicates(inplace=True)
        return df

    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """ drop selected columns from data frame

        Args:
            df (pd.DataFrame):  pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame columns dropped
        """
        for col in columns:
            df.drop(col, axis=1, inplace=True)
        return df

    def drop_rows(self, df: pd.DataFrame, column: str, row_value: str) -> pd.DataFrame:
        """drop rows in selected column based on condition given
        Args:
            df (pd.DataFrame): pandas data frame
            column (str): column label
            row_value (str): condition to check againest

        Returns:
            pd.DataFrame: pandas data frame with rows dropped
        """
        df = df.drop(df[df[column] != row_value].index)
        return df

    def columns_too_much_null(self, df: pd.DataFrame, percentage: int) -> pd.DataFrame:
        """drops columns with big persentage of null values

        Args:
            df (pd.DataFrame): pandas data frame
            percentage (int): persentage of null values

        Returns:
            [type]: pandas data frame columns dropped
        """
        columns = []
        for index, row in df.iterrows():
            if float(row["none_percentage"].replace("%", '')) > percentage:
                columns.append(index)

        return columns

    def convert_to_string(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to string

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """

        for col in columns:
            df[col] = df[col].astype("string")
        return df

    def convert_to_numbers(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to number

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = pd.to_numeric(df[col])
        return df

    def convert_to_integer(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to number

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = df[col].astype('int64')
        return df

    def convert_to_datetime(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to datetime

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = pd.to_datetime(df[col])
        return df

    def convert_to_boolean(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to boolean

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """

    def converter(self, df: pd.DataFrame, column, scale):
        """convert selected columns to scale
        df[column] = df[column] * scale
        return df

    def fix_missing_ffill(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(method='ffill')
        return df

    def fix_missing_bfill(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(method='bfill')
        return df

    def fill_with_mode(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].mode()[0])
        return df

    def fill_with_mean(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].mean())
        return df

    def fill_with_median(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].median())
        return df
    """
