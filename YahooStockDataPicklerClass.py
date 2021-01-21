# FILE YahooStockDataPicklerClass.py
# Downloads and pickles data from Yahoo
import pandas_datareader as data
import pickle
from datetime import datetime
from os.path import exists
import hashlib


class YahooStockDataPicklerClass:
    # Common generic filename
    __file_name: str = '../generic.pkl'
    __start_date: datetime = datetime(2018, 1, 1)
    __end_date: datetime = datetime.today()
    __tickers: list = ['AAPL', 'MSFT', '^GSPC']
    __date_format: str = "%d-%m-%Y"
    __pandas_data_format = "%Y-%m-%d"

    @staticmethod
    def pickle_tickers(**kwargs) -> data.DataReader:
        """
        Downloads and pickles tickers in argument
        :param tickers: list of tickers
        :param start_date: start date of your data
        :param end_date: end date of your data
        :param file_name: file name
        :return: dataframe with requested quotes
        """

        if 'tickers' in kwargs and kwargs['tickers'] is not None:
            tickers_arg: list = kwargs['tickers']
        else:
            tickers_arg: list = None
        tickers_arg = YahooStockDataPicklerClass.__check_return_tickers(tickers_arg)

        if 'start_date' in kwargs and kwargs['start_date'] is not None:
            start_date_arg: datetime = kwargs['start_date']
        else:
            start_date_arg: datetime = None
        start_date_arg = YahooStockDataPicklerClass.__check_return_start_date(start_date_arg)

        if 'end_date' in kwargs and kwargs['end_date'] is not None:
            end_date_arg: datetime = kwargs['end_date']
        else:
            end_date_arg: datetime = None
        end_date_arg = YahooStockDataPicklerClass.__check_return_end_date(end_date_arg)

        if 'file_name' in kwargs and kwargs['file_name'] is not None:
            file_name_arg: str = kwargs['file_name']
        else:
            file_name_arg: str = None

        file_name_local = YahooStockDataPicklerClass.__return_filename(tickers_arg, start_date_arg, end_date_arg,
                                                                       file_name_arg)
        fetched_data = data.DataReader(tickers_arg, 'yahoo',
                                       start=start_date_arg.strftime(YahooStockDataPicklerClass.__pandas_data_format),
                                       end=end_date_arg.strftime(YahooStockDataPicklerClass.__pandas_data_format))

        pickle.dump(fetched_data, open(file_name_local, 'wb'))

        return fetched_data

    # Reuse: load data
    @staticmethod
    def unpickle_tickers(filename_arg: str) -> data.DataReader:
        """
        Returns the file found under the specified path
        :param filename_arg: filename to search in the system
        :return:
        """
        if filename_arg is None:
            return pickle.load(open(YahooStockDataPicklerClass.__file_name, 'rb'))
        else:
            return pickle.load(open(filename_arg, 'rb'))

    @staticmethod
    def try_unpickle_tickers(**kwargs) -> data.DataReader:
        """
        Searches for the corresponding file in the system. If not found -> downloads data. If found -> returns data in
         the pickled file
        :param tickers: list of tickers
        :param start_date: start date of your data
        :param end_date: end date of your data
        :param file_name: file name
        :return: dataframe with all the quotes
        """

        if 'tickers' in kwargs and kwargs['tickers'] is not None:
            tickers_arg: list = kwargs['tickers']
        else:
            tickers_arg: list = None
        tickers_arg = YahooStockDataPicklerClass.__check_return_tickers(tickers_arg)

        if 'start_date' in kwargs and kwargs['start_date'] is not None:
            start_date_arg: datetime = kwargs['start_date']
        else:
            start_date_arg: datetime = None
        start_date_arg = YahooStockDataPicklerClass.__check_return_start_date(start_date_arg)

        if 'end_date' in kwargs and kwargs['end_date'] is not None:
            end_date_arg: datetime = kwargs['end_date']
        else:
            end_date_arg: datetime = None
        end_date_arg = YahooStockDataPicklerClass.__check_return_end_date(end_date_arg)

        if 'file_name' in kwargs and kwargs['file_name'] is not None:
            file_name_arg: str = kwargs['file_name']
        else:
            file_name_arg: str = None

        file_name_local = YahooStockDataPicklerClass.__return_filename(tickers_arg, start_date_arg, end_date_arg,
                                                                       file_name_arg)

        if exists(file_name_local):
            return YahooStockDataPicklerClass.unpickle_tickers(file_name_local)
        # else : download, pickle and return the file
        return YahooStockDataPicklerClass.pickle_tickers(tickers=tickers_arg, start_date=start_date_arg,
                                                         end_date=end_date_arg, file_name=file_name_local)

    @staticmethod
    def __return_filename(tickers_arg: list, start_date_arg: datetime, end_date_arg: datetime,
                          file_name_arg: str) -> str:
        """
        Creates and formats the filename based on the provided arguments.
        :param tickers_arg: list of tickers
        :param start_date_arg: start date of your data
        :param end_date_arg: end date of your data
        :param file_name_arg: file name
        :return: string with generated (unique) filename
        """
        file_name_local: str
        tickers_local = YahooStockDataPicklerClass.__check_return_tickers(tickers_arg)
        start_date_local = YahooStockDataPicklerClass.__check_return_start_date(start_date_arg)
        end_date_local = YahooStockDataPicklerClass.__check_return_end_date(end_date_arg)

        if file_name_arg is None and (tickers_local is not None
                                      and start_date_local is not None
                                      and end_date_local is not None):
            # Composed file name
            file_name_local = "{0}_{1}-{2}.pkl".format(YahooStockDataPicklerClass.__return_md5_string_hash(
                                                       '-'.join(tickers_local), length=10),
                                                       start_date_local
                                                       .strftime(YahooStockDataPicklerClass.__date_format),
                                                       end_date_local
                                                       .strftime(YahooStockDataPicklerClass.__date_format))
        elif tickers_local is None or start_date_local is None or end_date_local is None:
            print("Please note that the default datafile is unpickled!")
            # Default file name
            file_name_local = YahooStockDataPicklerClass.__file_name
        else:
            file_name_local = file_name_arg

        return file_name_local

    @staticmethod
    def __check_return_tickers(tickers_arg: list) -> list:
        """
        Private function checking if the tickers are empty. If they are-> returns the default value.
        :param tickers_arg:
        :return:
        """
        # Default tickers
        if tickers_arg is None:
            return YahooStockDataPicklerClass.__tickers
        else:
            return tickers_arg

    @staticmethod
    def __check_return_start_date(start_date_arg: datetime) -> datetime:
        """
        Private function checking if the dates are empty. If they are-> returns the default value.
        :param start_date_arg:
        :return:
        """
        # Default tickers
        if start_date_arg is None:
            return YahooStockDataPicklerClass.__start_date
        else:
            return start_date_arg

    @staticmethod
    def __check_return_end_date(end_date_arg: datetime) -> datetime:
        """
        Private function checking if the dates are empty. If they are-> returns the default value.
        :param end_date_arg:
        :return:
        """
        # Default tickers
        if end_date_arg is None:
            return YahooStockDataPicklerClass.__end_date
        else:
            return end_date_arg

    @staticmethod
    def __return_md5_string_hash(string_to_hash: str, **kwargs) -> int:
        """
        Returns a hash of string given in input (as integer)
        :param string_to_hash: text that will be hashed
        :param length: maximal length of the returned integer
        :return: int representing the provided string
        """
        if 'length' in kwargs and kwargs['length'] is not None and kwargs['length'] >= 10:
            # for some reason the length is + 2
            return int(hashlib.md5(string_to_hash.encode('utf-8')).hexdigest()[:kwargs['length'] - 1], 16)
        else:
            return int(hashlib.md5(string_to_hash.encode('utf-8')).hexdigest()[:15], 16)
