import logging
import snap7

# Configure o endereço IP do dispositivo LOGO e a área de memória a ser lida ou escrita
plc_address = "192.168.0.10"
db_number = 1

# Configure as entradas e saídas digitais a serem lidas e escritas
input_address = 0  # Endereço do byte de entrada
output_address = 2  # Endereço do byte de saída

# Configurar o log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar conexão com o LOGO!
plc = snap7.logo.Logo()
plc.connect(plc_address, 0x0300, 0x0200)

# Verificar se a conexão foi estabelecida
if plc.get_connected():
    logger.info("Conexão estabelecida com o LOGO!")

    # # Ler o valor do byte de entrada especificado
    # input_byte = plc.read_area(snap7.types.Areas.PA, db_number, input_address, 1)

    # # Mostrar o valor do byte de entrada lido
    # logger.info(f"Valor do byte de entrada: {int.from_bytes(input_byte, byteorder='big')}")

    # Escrever um valor no byte de saída especificado
    # output_byte = b'\x00'  # Configurar o byte de saída para '0'
    # plc.write_area(snap7.types.Areas.PE, db_number, output_address, output_byte)

    # # Ler o valor do byte de saída especificado para verificar se a escrita foi bem-sucedida
    # output_byte_read = plc.read_area(snap7.types.Areas.PE, db_number, output_address, 1)

    # # Mostrar o valor do byte de saída lido
    # logger.info(f"Valor do byte de saída: {int.from_bytes(output_byte_read, byteorder='big')}")

else:
    logger.error("Conexão falhou")

# Desconectar do LOGO!
plc.disconnect()
logger.info("Desconectado do LOGO!")
plc.destroy()
