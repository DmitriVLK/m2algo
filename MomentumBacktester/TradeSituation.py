from MomentumBacktester.Quote import Quote


class TradeSituation:
    # This variable will be incremented after each call of TradeSituation.generate_next_id().
    # It is used to populate __trade_situation_id.
    __common_trade_situation_id: int = 0
    # Instance attributes
    # Unique ID of the trade_situation
    __trade_situation_id: int
    # If True: it's a LONG (BUY) trade. If False: it's a SHORT (SELL) trade.
    __is_long_trade: bool
    # Quote saved when we opened the position
    __executed_open_quote: Quote
    # Quote saved when we close the position
    __executed_close_quote: Quote
    # Flag used to describe if the position is opened or closed
    __is_closed: bool
    # Maximum draw down in basis points. Always positive!
    __max_dd_in_bps: float
    # Latest profit or loss of the position in basis points
    __pnl_bps: float
    # Take profit in basis points
    __take_profit_in_bps: float

    def __init__(self, open_order_arg: Quote, is_long_trade_arg: bool, take_profit_in_bps_arg: float):
        # Init locals

        # Update and set the __trade_situation_id
        self.__trade_situation_id = TradeSituation.generate_next_id()
        # Check arguments sanity.

        #    raise Exception("Please note that the take profit has to be positive (:2.2f)"
        #                    .format(take_profit_in_bps_arg))

        # Call self.open_position(...) to open the position immediately

    def open_position(self, quote_arg: Quote):
        """
        Flags the is_closed to False. Saves the entry order.
        :param quote_arg: quote class's instance expected. The first quote.
        :return:
        """
        # Sets the __executed_open_quote to argument's value and flags __is_closed to FALSE
        pass

    def close_position(self, quote_arg: Quote):
        """
        Flags the position as closed. Calculates final PnL
        :param quote_arg: last quote
        :return:
        """
        # Sets the __executed_close_quote to argument's value, calculates PNL and flags __is_closed to TRUE
        pass

    def update_on_order(self, quote_arg: Quote) -> bool:
        """
        Updates all the variables in the position. Calculates the PnL.
        :param quote_arg: the latest quote
        :return: returns True if the position was closed (target profit reached)
        """
        # Check if the position is alive. Return false if the position is dormant

        # Check/update current pnl and draw down

        # Check if target pnl was reached

            # Target pnl reached: close position; set __is_closed accordingly

            # Return True

        # PnL target not reached: return false
        return False

    def calculate_pnl_and_dd(self, quote_arg: Quote) -> float:
        """
        Calculates (and updates) the PnL and draw down for the position
        :param quote_arg: the current quote
        :return: current pnl
        """
        # In case the position is not opened (not alive) return the value stored in __pnl_bps

        # Calculate pnl (different for LONG and SHORT)

        # Calculate draw down

        # return __pnl_bps
        return 0.0

    def return_current_pnl(self) -> float:
        """
        Returns the current (or final if the position is closed) pnl.
        :return:
        """
        return 0.0

    def return_current_draw_down(self) -> float:
        """
        Returns the current (or final if the position is closed) maximum draw down.
        :return:
        """
        return 0.0

    def trade_situation_id(self) -> int:
        """
        Returns this trade situation ID
        :return:
        """
        return self.__trade_situation_id

    def is_closed(self):
        """
        Returns true if the position was closed previously
        :return:
        """
        return True

    @staticmethod
    def generate_next_id():
        TradeSituation.__common_trade_situation_id += 1
        return TradeSituation.__common_trade_situation_id


