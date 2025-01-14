from nfstream import NFPlugin

class FirstPacketPayloadLen(NFPlugin):
    '''FirstPacketPayloadLen | First packet's payload length per direction,
    note that the first packet is always from src to dst hence
    bidirectional first packet's payload length is equal to src2dst_packet_payload_len.
    if there are no packets from dst to src, then the value is defaulted to None (empty).
        
    Output Features:
        1. src2dst_first_packet_payload_len
        2. dst2src_first_packet_payload_len
        

    '''
    def __init__(self, **kwargs):
        ''' '''
        super().__init__(**kwargs)

    def on_init(self, packet, flow):
        ''' '''
        flow.udps.src2dst_first_packet_payload_len = packet.payload_size
        flow.udps.dst2src_first_packet_payload_len = None
        
    def on_update(self, packet, flow):
        ''' '''
        if flow.udps.dst2src_first_packet_payload_len is None and packet.direction == 1:
            flow.udps.dst2src_first_packet_payload_len = packet.payload_size 
