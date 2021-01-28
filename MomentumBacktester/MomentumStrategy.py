from MomentumBacktester.FifoDoublesList import FifoDoublesList
from MomentumBacktester.Quote import Quote
from MomentumBacktester.TradeSituation import TradeSituation


class MomentumStrategy:
    # This variable will be incremented after each call of TradeSituation.generate_next_id().
    # It is used to populate __trade_situation_id.
    __common_momentum_strategy_id: int = 0
    # Unique ID of the momentum strategy
    __strategy_id: int
    # Set to final value in constructor.
    __ma_slow_var: int
    __ma_fast_var: int

    # Set to final value in constructor.
    __ma_slow_fifo_list: FifoDoublesList
    __ma_fast_fifo_list: FifoDoublesList

    # Position is open in this way currently
    # False: sold
    # True: bought
    __current_trading_way: bool

    # Currently opened position
    __open_position: TradeSituation

    # List of trade situation
    __positions_history: list

    # This variable is set once to True when the required (minimal) data points are populated into fifo_list(s)
    __is_filled_start_data: bool
    __filled_data_points: int

    def __init__(self, ma_slow: int, ma_fast: int, target_profit_arg: float):
        """
        Initializes the trading strategy calculator. Please feed it with arguments for your moving average trading
        strategy. The MA_SLOW > MA_FAST. By construction the FAST average is low-period.
        :param ma_slow: slow moving moving average
        :param ma_fast: fast moving moving average
        :param target_profit_arg: target profit for this strategy
        """
        self.__strategy_id = MomentumStrategy.generate_next_id()
        # Arguments sanity check

        #    raise Exception("The Moving average fast ({0}) has to be lower than the Moving average slow ({1})"
        #                    .format(ma_fast, ma_slow))

        #    raise Exception("The Moving average fast and slow ({0} and {1}) have to be more that 0"
        #                    .format(ma_fast, ma_slow))
        # Save input arguments

        # Init the FiFo arrays (FifoDoublesList class)

        # Init locals

    def step(self, quote: Quote):
        """
        Calculates the indicator and performs update/open/close action on the TradeSituation class
        (representing investment position)
        :param quote: float; the price of the invested stock
        :return: no return
        """
        # Update values (prices) in the fifo_lists (with put method)

        # Update position with arrived quote

            # We closed the position (returns true if the position is closed)

        # The fifo_list(s) are filled?

            # Calculate fast and slow lists means

            # If MA short > MA long => BUY
            # If MA long > MA short => SELL
            # You must not reopen the position if the trading direction (__current_trading_way) has not changed.

                # Buy: open position if there is none; close the position if it's hanging in the other way; append the
                # positions history (to save how much it gained); save the new __current_trading_way

                # Sell (repeat for SELL)

         #Else: the fifo lists are note filled
            # The fifo_list(s) are not yet filled. Do the necessary updates and checks

    pass

    def close_pending_position(self, quote: Quote):
        """
        Called at the end of the program execution. Checks if the position is still opened and closes that position.
        :param quote: last quote available in the data set
        :return:
        """
        # If there is still a position --> close it with the quote provided to you in arguments.
        pass

    def all_positions(self) -> list:
        """
        Returns the positions_history object
        :return:
        """
        # Returns __positions_history
        return []

    def get_ma_slow(self) -> int:
        """
        Returns the value of slow MA
        :return:
        """
        return 0

    def get_ma_fast(self) -> int:
        """
        Returns the value of fast MA
        :return:
        """
        return 0

    def get_target_profit(self) -> float:
        """
        Returns the target profit of this strategy
        :return:
        """
        return 0.0

    def get_strategy_id(self):
        """
        Returns the (local) unique strategy ID.
        :return:
        """
        return self.__strategy_id

    @staticmethod
    def generate_next_id():
        MomentumStrategy.__common_momentum_strategy_id += 1
        return MomentumStrategy.__common_momentum_strategy_id
