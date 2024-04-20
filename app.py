from vetiver import VetiverModel, VetiverAPI
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

import logging
logging.basicConfig(
  format='%(asctime)s - %(message)s',
  level=logging.INFO
)
logging.info("App Started")

load_dotenv(find_dotenv())

b = pins.board_folder('data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240418T093928Z-cf3d4')

app = VetiverAPI(v, check_prototype = True)
app.run(port = 8080)
