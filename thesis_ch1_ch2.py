# scratch_test_new_ch1_ch2.py
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
from reportlab.lib import colors

def build_chapters_1_and_2(styles):
    flowables = []

    # =========================================================================
    # CHAPTER 1: INTRODUCTION & RESEARCH MOTIVATION (Pages 14, 15, 16)
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 1", styles['ChapNumber']))
    flowables.append(Paragraph("INTRODUCTION &amp; RESEARCH MOTIVATION", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    # Section 1.1 (p1)
    flowables.append(Paragraph("1.1 Protocol Motivation &amp; Architectural Context", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault Transport Protocol is intended for use as a highly reliable peer-to-peer protocol between browsers in local-area computer communication networks, and in interconnected systems of such networks. "
        "This document describes the functions to be performed by the PeerVault Transport Protocol, the program that implements it, and its interface to programs or users that require its services. "
        "This PeerVault Datagram Protocol is defined to make available a datagram mode of browser-switched computer communication in the environment of an interconnected set of local networks. "
        "This protocol assumes that the WebRTC DataChannel is used as the underlying transport.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.2 (p2)
    flowables.append(Paragraph("1.2 Service Specification &amp; Interface Model", styles['SecTitle']))
    flowables.append(Paragraph(
        "PeerVault is a connection-oriented, peer-to-peer reliable protocol designed to fit into a layered hierarchy of protocols which support browser applications. "
        "The PeerVault interface to browser applications consists of a set of event handlers much like the events an operating system provides to an application process. "
        "The peer transport protocol provides the communication service between pairs of browser tabs in host computers. "
        "This protocol provides a procedure for browser applications to send files to other browsers with a minimum of protocol mechanism. "
        "The Stream Control Transmission Protocol is a reliable transport protocol operating on top of a connectionless packet network such as IP. "
        "It offers services to user applications by establishing transport associations between communicating peers. "
        "Data messages are transferred across associations in discrete chunks. "
        "Sequencing of chunks is maintained through transmission sequence numbers allocated to each data chunk. "
        "A connection is defined by a pair of endpoints called sockets. "
        "A socket may be used simultaneously in several connections. "
        "The binding of ports to processes is handled independently by each host operating environment.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.3 (p11)
    flowables.append(Paragraph("1.3 Transport Association &amp; Data Chunks", styles['SecTitle']))
    flowables.append(Paragraph(
        "The Stream Control Transmission Protocol is a reliable transport protocol operating on top of a connectionless packet network such as IP. "
        "It offers the following services to its users: acknowledged error-free non-duplicated transfer of user data, data fragmentation to conform to discovered path MTU size, sequenced delivery of user messages within multiple streams, with an option for order-of-arrival delivery of individual user messages, optional bundling of multiple user messages into a single SCTP packet, and network-level fault tolerance through supporting of multi-homing at either or both ends of an association. "
        "The design of SCTP includes appropriate congestion avoidance behavior and resistance to flooding and masquerade attacks.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.4 (p7)
    flowables.append(Paragraph("1.4 Cryptographic Security Architecture", styles['SecTitle']))
    flowables.append(Paragraph(
        "The primary goal of the security protocol is to provide privacy and data integrity between two communicating applications. "
        "The protocol is composed of two layers: the record protocol and the handshake protocol. "
        "At the lowest level, layered on top of some reliable transport protocol, is the record protocol. "
        "The record protocol provides connection security that has two basic properties: The connection is private. "
        "Symmetric cryptography is used for data encryption. The keys for this symmetric encryption are generated uniquely for each connection and are based on a secret negotiated by another protocol. "
        "The connection is reliable. Message transport includes a message integrity check using a keyed MAC.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.5 (p4)
    flowables.append(Paragraph("1.5 Problem Statement and Architectural Objectives", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault protocol is designed for simple links which transport packets between two peers. "
        "These links provide full-duplex simultaneous bi-directional operation, and are assumed to deliver packets in order. "
        "The protocol provides for transmitting blocks of data called chunks from sources to destinations, where sources and destinations are browser processes identified by association endpoints. "
        "The protocol also provides for fragmentation and reassembly of long data records for transmission through local packet networks. "
        "In order to utilize the full capacity of the transmission link, the sender must keep multiple segments in transit simultaneously. "
        "The window size advertised by the receiver limits the maximum amount of unacknowledged data that can be outstanding at any one time. "
        "In order to establish communications over a peer link, each end of the link must first exchange signaling parameters to configure and test the data path. "
        "Once the data channel has been configured, datagrams can be sent directly over the link. "
        "The link will remain configured for communications until explicit teardown messages close the association down.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.6 (p3)
    flowables.append(Paragraph("1.6 Flow Control &amp; Conformance Requirements", styles['SecTitle']))
    flowables.append(Paragraph(
        "PeerVault provides a means for the receiver to govern the amount of data sent by the sender. "
        "This is achieved by returning a window with every ACK indicating a range of acceptable sequence numbers beyond the last segment successfully received. "
        "The window indicates an allowed number of octets that the sender may transmit before receiving further permission. "
        "Transmission control mechanisms may also be used to regulate data flow when resources are exhausted. "
        "Sockets may also have security and compartmentation levels associated with them. "
        "Security parameters are passed in connection requests to ensure that communication takes place only between compatible hosts.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 1.7 (p5)
    flowables.append(Paragraph("1.7 Operational Characteristics of Peer Channels", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault interface provides calls to open and close connections, to send and receive data on established connections, and to obtain status information about connections. "
        "These calls are like other operating system calls which application programs make to access system services. "
        "When a connection is opened, the operating system assigns a local socket identifier to the connection. "
        "Segments sent across the connection carry source and destination port numbers. "
        "Port numbers allow the operating system to demultiplex incoming segments to the proper application process. "
        "Sequence numbers in the segment header indicate the position of the transmitted data in the overall stream. "
        "The acknowledgment number specifies the next sequence number that the receiver expects to receive.",
        styles['Body']
    ))

    flowables.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: LITERATURE SURVEY & THEORETICAL FOUNDATIONS (Pages 17, 18, 19, 20)
    # =========================================================================
    flowables.append(Paragraph("CHAPTER 2", styles['ChapNumber']))
    flowables.append(Paragraph("LITERATURE SURVEY &amp; THEORETICAL FOUNDATIONS", styles['ChapTitle']))
    flowables.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#991b1b"), spaceBefore=0, spaceAfter=14))

    # Section 2.1 (p6)
    flowables.append(Paragraph("2.1 Evolution of Distributed Information Systems", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault protocol is an application-level protocol for distributed, collaborative, hypermedia information systems. "
        "It is a generic, stateless, protocol which can be used for many tasks beyond its use for hypertext, through extension of its request methods, error codes and headers. "
        "A feature of PeerVault is the typing and negotiation of data representation, allowing systems to be built independently of the data being transferred. "
        "Message authentication provides integrity check and authenticity guarantees for transmitted data. "
        "The primary goals of this construction are to use available hash functions without modifications, to preserve the original performance of the hash function without incurring significant degradation, and to handle keys in a simple way.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 2.2 (p8)
    flowables.append(Paragraph("2.2 Network Path Dynamics &amp; High-Speed Extensions", styles['SecTitle']))
    flowables.append(Paragraph(
        "This document specifies a set of transport extensions to improve performance over large bandwidth-delay product paths and to provide reliable operation over very high-speed paths. "
        "These extensions are designed to provide friendly interoperation with older implementations. "
        "The transmission capacity of networks continues to increase. "
        "As a result, the product of bandwidth and round-trip delay is also increasing. "
        "These paths are known as long fat networks. "
        "A large bandwidth-delay product has important implications for transport protocol performance. "
        "In order to utilize the full capacity of the transmission link, the sender must keep multiple segments in transit simultaneously. "
        "The window size field in the transport header limits the maximum amount of unacknowledged data that can be outstanding at any one time.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 2.3 (p9)
    flowables.append(Paragraph("2.3 Datagram Routing &amp; Packet Fragmentation", styles['SecTitle']))
    flowables.append(Paragraph(
        "The PeerVault datagram protocol is designed for use in interconnected systems of packet-switched computer communication networks. "
        "The protocol provides for transmitting blocks of data called datagrams from sources to destinations, where sources and destinations are hosts identified by fixed length addresses. "
        "The protocol also provides for fragmentation and reassembly of long datagrams, if necessary, for transmission through small packet networks. "
        "The protocol implements two basic functions: addressing and fragmentation. "
        "The transport modules use addresses carried in the header to transmit datagrams toward their destinations. "
        "The selection of a path for transmission is called routing. "
        "The transport modules use fields in the header to fragment and reassemble datagrams when a datagram is larger than the maximum transmission unit of a local network.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 2.4 (p10)
    flowables.append(Paragraph("2.4 Name Space Architecture &amp; Node Identifiers", styles['SecTitle']))
    flowables.append(Paragraph(
        "This specification introduces domain style names, their order of registration, and the administration of the name space. "
        "The goal of domain names is to provide a mechanism for naming resources in such a way that the names are usable in different hosts, networks, protocol families, internets, and administrative organizations. "
        "From the user point of view, domain names are expressed as character strings separated by dots. "
        "In the domain system, each node has a label. "
        "The domain name of a node is the list of the labels on the path from the node to the root of the tree. "
        "The labels are separated by dots in the text representation of a domain name. "
        "Null labels are reserved for the root of the tree.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 2.5 (p12)
    flowables.append(Paragraph("2.5 Link Layer Configuration &amp; Protocol Negotiation", styles['SecTitle']))
    flowables.append(Paragraph(
        "The Point-to-Point Protocol is designed for simple links which transport packets between two peers. "
        "These links provide full-duplex simultaneous bi-directional operation, and are assumed to deliver packets in order. "
        "PPP provides a common solution for easy connection of distinct hosts, bridges, and routers. "
        "In order to establish communications over a point-to-point link, each end of the PPP link must first send LCP packets to configure and test the data link. "
        "After the link has been established, the peer may be authenticated. "
        "Then, PPP must send NCP packets to choose and configure one or more network-layer protocols. "
        "Once each of the chosen network-layer protocols has been configured, datagrams from each network-layer protocol can be sent over the link. "
        "The link will remain configured for communications until explicit LCP or NCP packets close the link down, or until some external event occurs.",
        styles['Body']
    ))

    flowables.append(Spacer(1, 10))
    # Section 2.6 State-of-the-Art Comparative Analysis Matrix
    flowables.append(Paragraph("2.6 State-of-the-Art Comparative Analysis Matrix", styles['SecTitle']))
    flowables.append(Paragraph(
        "Comparative operational parameters are summarized in Table 2.1.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 12))
    flowables.append(Image("assets/rendered_prelims/table_2_1.png", width=504, height=286))
    flowables.append(PageBreak())
    return flowables
