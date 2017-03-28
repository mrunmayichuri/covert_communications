# covert_communications

I have implemented a covert channel using the TCP destination port field. To identify whether a packet is a covert message, I have enabled the “E” (ECN/Explicit Congestion Notification) flag. The server program constructs the message such that the ‘E’ (ECN/Explicit Congestion Notification) flag is set so that the client will be able to identify that it is a covert message. The constructed message is stored in the destination ports field of the TCP header.
