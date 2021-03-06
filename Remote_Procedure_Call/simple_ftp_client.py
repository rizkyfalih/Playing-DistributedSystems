import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.1.8:8000") # initialization the network and the port
with open("test.txt",'rb') as handle: # open the file that you want to be upload (must 1 folder in the client) 
    data = xmlrpc.client.Binary(handle.read()) # read the file and change it to be binary form
    handle.close() # close the handle when the file has been read
    result = proxy.file_upload(data) # send the binary form file with call the 'file_upload function' from server to server

handle = open("Server/Download1.txt","wb") # find the file in server ('The file must be in server/1 folder in server')
handle.write(proxy.download().data) # download the file from server
handle.close() # close the handle when the file was downloaded 