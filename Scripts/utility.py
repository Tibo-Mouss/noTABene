
from PIL import Image
import pickle


def DisplayImage(image):
  #read the image
  #im = Image.open("D:/Documents/GitHub/noTABene/Scripts/test_img.png")
  #show image
  image.show()

def PackData(data):
  return pickle.dumps(data)

def UnPackData(data):
  return pickle.loads(data)



import asyncio

async def tcp_echo_client(message):
  reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

  print(f'Send: {message!r}')
  writer.write(message.encode())
  await writer.drain()

  data = await reader.read(100)
  print(f'Received: {data.decode()!r}')

  print('Close the connection')
  writer.close()
  await writer.wait_closed()



async def handle_echo(reader, writer):
  data = await reader.read(100)
  message = data.decode()
  addr = writer.get_extra_info('peername')

  print(f"Received {message!r} from {addr!r}")

  print(f"Send: {message!r}")
  writer.write(data)
  await writer.drain()

  print("Close the connection")
  writer.close()

async def main():
  server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

  addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
  print(f'Serving on {addrs}')

  async with server:
      await server.serve_forever()

