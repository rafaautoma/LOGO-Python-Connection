import snap7

# Cria o cliente snap7
plc = snap7.client.Client()

# Conecta com o LOGO! na porta TCP 102
plc.connect('192.168.0.10', 0, 102)

# Escreve o valor 1 na saída Q0.0
plc.write_area(snap7.types.Areas.PB, 0, 0, bytearray([0x01]))

# Fecha a conexão com o LOGO!
plc.disconnect()
