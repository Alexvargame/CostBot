from aiogram import executor
from dispatcher import dp
import handlers



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
