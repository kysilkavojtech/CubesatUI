TCP:

TCP is a communications protocol that will let us pass information between GNU Radio flowgraphs and Python scripts where our pass control control will eventually be.
In a python script, we can set up a "server" program. Essentially, this server is given a port number to listen to. Then, in GR, we can set up a client program.
The client sends a connect request to the server which establishes communication. Once paired, the server and client are equal. Both can send and receive.

To use the stuff here, first run the server code, and execute either the send or receive GR client flowgraph. 
*note: for some reason, when we use a flowgraph that is sending and receiving, stuff doesn't work*
