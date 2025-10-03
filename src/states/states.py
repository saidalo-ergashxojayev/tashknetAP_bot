from aiogram.fsm.state import State, StatesGroup


class StatesGroup(StatesGroup):
    MM = State() #main_menu
    ChL_ChD = State() #checking live > choosing district
    GHD = State() #getting_historical_data
    HD_D = State() #historical_data > choosing district
    HD_DT = State() #historical_data > choosing date and time 