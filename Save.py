import pickle
import json
import msgpack

file_path = 'C:\\Users\\csarb\\AppData\\LocalLow\\TiramisuLovesNtr\\Ntraholic\\ntraholic2_1_20.dontdeletethisdata'

# Intenta deserializar utilizando diferentes bibliotecas
try:
    # Intenta con pickle
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        print('Deserialización exitosa con pickle:')
        print(data)
except:
    try:
        # Intenta con json
        with open(file_path, 'r') as file:
            data = json.load(file)
            print('Deserialización exitosa con json:')
            print(data)
    except:
        try:
            # Intenta con msgpack
            with open(file_path, 'rb') as file:
                data = msgpack.unpack(file)
                print('Deserialización exitosa con msgpack:')
                print(data)
        except:
            print('No se pudo deserializar el archivo con ninguna biblioteca conocida.')
                
