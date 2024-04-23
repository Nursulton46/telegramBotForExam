# dic = {'1': ['In a packet network , the routing is',
#              'The process used for determining the source-destination routes taken by packets ,i.e for writing the '
#              'routing table'],
#        '2': ['After having identified the correct output port, an IP router',
#              'Modifies the Time To Live and Header Checksum field of the datagram header;'],
#        '3': ['The congestion control of the Transmission Control Protocol (TCP) is based',
#              'On the adjustment of the transmission window size according  to the memory availability at the receiver'],
#        '4': ['The IP header, i.e., the IP PCI , mandatory contains.',
#              'The Time To Live (TTL) field that enables removing from the network packets that were fro-waded by Too '
#              'many routers'],
#        '5': ['End-to-end error recovery over the Internet, when available',
#              'is implement at the Transport Layer'],
#        '6': ['The IP protocol provides a service that is',
#              'Unreliable (i.e.,without any delivery guarantee) and connectionless'],
#        '7': ['Which of the following claims is false?',
#              'A host transmits IP packets only to hosts whose net_id is equal to its own net_id.'],
#        '8': [
#            'If a router receives an IP packet with correct checksum ,TTL=9 , and equal IP source and IP destination '
#            'addresses',
#            'It forwards the packet to the destination,but it sends an ICMP message to the source to notify the error'],
#        '9': ['TCP segments',
#              'Have a variable size that is selected on the basis of the congestion level in the network'],
#        '10': [
#            'Lets consider a host who is transmitting data by means of TCP .Give a current value for the transmission '
#            'window size equal to 10 segments , with a maximum receive window equal to 40 segments, when the sender '
#            'receives a segment containing an acknowledgment from the receiver , which to the following situations is '
#            'impossible?',
#            'The current value of the transmission window size becomes equal to 51 segments'],
#        '11': ['In the CSMA/CD protocol, a station completes the transmission of a frame',
#               'Only if , sensing the channel, it doesnt detect an eventual simultaneous reception with the current '
#               'transmission'],
#        '12': ['The Address Resolution Protocol (ARP)',
#               'achieves a translation function between layer-3 addresses and layer-2 addresses'],
#        '13': [
#            'Which among the following is a distinctive function of the Link Layer in a networking layered architecture?',
#            'Delivery of packets (referred to as frames at this layer) among neighboring nodes'],
#        '14': ['The IP version 4 addresses are:',
#               'Of fixed total length,but consisting of a variable length part identifying the network and a variable '
#               'length part identifying the host'],
#        '15': ['The Network Layer', 'Is over the Link Layer and below the Transport Layer'],
#        '16': ['A network protocol is', 'A set of rules that devices must use for communications'],
#        '17': ['The destination IP address in an IP packet is',
#               'A fundamental header field, used by routers to forward the packet'],
#        '18': ['A DHCP server deployed in a local area network provides',
#               'An IP configuration to hosts connected to the local area network;'],
#        '19': ['The throughput (i.e., the amount of transferred bits per second ) offered to a traffic flow',
#               'Is given by the lowest throughput offered in all the traversed link, i.e., the bottleneck'],
#        '20': ['The header of a data packet in a packed switching network with datagram service includes',
#               'The address of the source and destinations nodes '],
#        '21': ['The end-to-end delay in a computer network', 'Depends on the network load'],
#        '22': ['An Ethernet switch , when it receives an ARP request packet',
#               'Forwards it only on all ports, except the one over which the packet has been received'],
#        '23': ['The DSL access network separates data and phone calls on the same transmission media between the user '
#               'equipments and the ISP equipments using',
#               'Frequency division multiplexing'],
#        '24': ['Layered protocol architectures', 'Are widely used because the ensure scalability and simplicity'],
#        '25': ['The flow control in the TCP protocol',
#               'is based on some information included into the segments sent from the receiver to the sender'],
#        '26': ['In a Stop&Wait transmission protocol',
#               'A device can send only one packet and then it has to stop, waiting for an acknowledge'],
#        '27': ['The Ethernet technology', 'Can be based on switches in order to obtain better performance'],
#        '28': ['In a Sliding Window transmission protocol(e.g., Go-Back-N)',
#               'A device can send out an arbitrary number of packets without awaiting for acknowledges'],
#        '29': ['The POP3 Protocol',
#               'Can be used to transfer electronic mail messages from a server to a client installed on a PC'],
#        '30': ['The Internet network', 'Is based on packet switching'],
#        '31': ['During the slow-start phase of the TCP congestion control, the transmission window size of the sender',
#               'doubles at every received acknowledgment'],
#        '32': ['The reception on a node A of an ICMP Echo Reply packet sent by a node B states that',
#               'A and B can exchange IP packets'],
#        '33': [
#            'The TCP segments that are sent from a host A to a host B include an acknowledgement number that specific',
#            'The next byte host A is willing to receive in the segments sent by host B'],
#        '34': ['The HEAD method of the HTTP protocol is used to:', 'receive only the header of the HTTP request'],
#        '35': ['A possible IP network that can be assigned to an Ethernet network containing 200 nodes is',
#               '130.192.2.0/24'],
#        '36': ['In a packet switched network, the routing is',
#               'The process used for determining the source-destination routes taken by packets , i.e., for writing '
#               'the routing'],
#        '37': ['Two IP nodes 130.192.40.1/24 e 130.192.40.200/24', 'Can directly exchange IP packets'],
#        '38': ['The ARP Request frame is used to learn:',
#               'The MAC address of an IP node directly connected to the source noded'],
#        '39': ['The IP protocol:',
#               'allows a large size network to be more scalable thanks to the address aggregation feature'],
#        '40': ['SMTP (Simple Mall Transfer Protocol)',
#               'allows an email server to communicate with another server who is the sender of a given message'],
#        '41': ['Congestion control in TCP', 'Limits the size of the transmission window'],
#        '42': ['The Internet Control Message Protocol (ICMP) allows',
#               'the exchange of error messages among routers and hosts.'],
#        '43': ['IP version 4 addresses are:',
#               'usually assigned on geographical and topological basis in order to favor aggregation'],
#        '44': ['Flow control', 'Is offered by TCP, using a dedicated field in the header of the segment'],
#        '45': ['The DHCP protocol', 'is used to automatically configure an IP host'],
#        '46': ['The slow start phase in TCP',
#               'Allows the congestion window to grow rapidly starting from a very low initial value'],
#        '47': ['The DNS (Domain Name System)',
#               'Is a server installed inside a corporate network and it contains the association between the name and '
#               'the address of any host in the Internet'],
#        '48': ['TCP segments include a sequence number that specifies',
#               'The position of the first byte of the segment in the sequence of byte transmitted over the TCP '
#               'connection'],
#        '49': ['A client operating according to the Go-Back-N protocol (based on packets)',
#               'Retransmits all unacked packets whenever a timer expires.'],
#        '50': ['A client operating according to the Stop&Wait protocol',
#               'Can send a given byte only after the reception of the acknowledge corresponding to the previous one '
#               'sent over the network'],
#        '51': ['A client operating according to the Stop&Wait protocol',
#               'Is equivalent to pipelined protocol with window size equal to I'],
#        '52': ['A digital signature of a document is composed by',
#               'A plaintext document and message digest ciphered with the senders private key'],
#        '53': ["A message digest or hash function H can be considered 'good' if",
#               'It is computationally infeasible to find any two different messages x and y such that H(x)=H(y)'],
#        '54': ['An Ethernet switch is', 'A network node that forwards frame on the basis of the MAC address'],
#        '55': ['A client operating according to the Stop&Wait protocol', 'Is based on a sliding window technique'],
#        '56': ['A peer-to-peer file sharing system',
#               "Is 'self-scalable' even if it uses a centralized indexing server as the server is not involved in resource downloads"],
#        '57': ['A BitTorrent peer', 'Connects to a subset of the peers belonging to a given torrent'],
#        '58': ['A client operating according to the Selective-Repeat protocol (based on packets)',
#               'Retransmits only the packet that caused the timer expiration'],
#        '59': ['A web cache on a proxy server',
#               'May be used for saving bandwidth in the access link of an enterprise network'],
#        '60': ['A router is', 'A network node that is able to forward datagrams.'],
#        '61': ['A message digest or hash function H', 'Produces a fixed length output'],
#        '62': ['A client operating according to the Stop&Wait protocol',
#               'Can send a given byte only after the reception of the acknowledge corresponding to the previous one '
#               'sent over the network'],
#        '63': ['A client operating according to the Go-Back-N protocol (based on packets)-',
#               'Retransmits all unacked packets whenever a timer expires'],
#        '64': ['Consider a web application, which of the following claim is true?',
#               'Web applications are not optimized for performance'],
#        '65': ['Consider a web application which of the following  claims is true',
#               'Web application are normally allowed by firewalls'],
#        '66': ['In an asymmetric key cryptography scheme', 'The public key is made of two numbers'],
#        '67': ['In a symmetric key cryptography scheme',
#               'The sender and the receiver must agree upon a key before starting secure Communication'],
#        '68': ['In an asymmetric key cryptography scheme',
#               'An attacker cannot mount a man in the middle attack if certificates and certification authorities are '
#               'involved'],
#        '69': ['In an asymmetric key cryptography scheme',
#               'The involved actors must agree upon a common key before starting secure communication'],
#        '70': ['In an asymmetric key cryptography scheme',
#               'Public and private part of a key pair are derived from two prime numbers'],
#        '71': ['In a routing table, the next-hop column of a static route is',
#               'The IP address of a remote interface directly connected to the router.'],
#        '72': ['In a peer-to-peer file sharing system',
#               'There could be a centralized server for the indexing of the available resources, but this feature '
#               'might also be implemented directly on the peers.'],
#        '73': ['route is', 'The IP address of a local interface.'],
#        '74': ['In a peer-to-peer file sharing system', 'The overall download speed might depend on the number of peers '
#                                                        'in the system'],
#        '75': ['The circuit switching technology', 'Provides deterministic delivery in terms of end-to-end delay'],
#        '76': ['The HTTP Protocol', 'Is based on messages that include a set of headers'],
#        '77': ['The HTTP Protocol', 'Can handle the transfer of files between a server and client'],
#        '78': ['The HTTP Protocol', 'Can be used to transfer files.'],
#        '79': ['The SMTP Protocol', 'Is used for the delivery of outgoing emails from a client to a given server'],
#        '80': ['SMTP Protocol', 'Is based on clear-text messages.'],
#        '81': ['The SMTP Protocol', 'Uses text based messages from a client to a server and vice verse'],
#        '82': ['The UDP Protocol', 'Does not use a sequence number'],
#        '83': ['The POP3 protocol', 'Is not used while reading emails in a webmail system'],
#        '84': ['The POP3 Protocol',
#               'Can be used to transfer emails from a server to an email client installed on a PC'],
#        '85': ['The FTP Protocol', 'Uses one or more TCP connections'],
#        '86': ['The TCP Protocol', 'Is able to recover from packet losses.'],
#        '87': ['The TCP Protocol',
#               'Adopts a sequence number that '
#               'keeps trace of the amount of '
#               'bytes already transmitted'],
#        '88': ['The FTP protocol', 'Can provide data encryption if its secure version based on SSL is used'],
#        '89': ['The packet switching technology', 'Ensures efficient bandwidth utilization'],
#        '90': ['The Transport Layer of the Internet protocol stack', 'Might open connections before sending data'],
#        '91': ['The Ethernet technology', 'Is based on the CSMA/CD protocol'],
#        '92': ['The Link Layer of the Internet protocol stack',
#               'Handles frame transmission by also defining transmission rules'],
#        '93': ['The Network Layer of the Internet protocol stack', 'Handles end-to-end delivery of data'],
#        '94': ['The Network Layer of the Internet protocol stack', 'Is based on the IP protocol'],
#        '95': ['The Ethernet technology', 'Can be used to delivery data between two locally connected nodes'],
#        '96': ['Which of the following claims is true',
#               'Packets of VPN are encrypted before entering  public internet'],
#        '97': ['What is the typical role of IPsec in VPNs',
#               'To open an manage secure tunnels across the public internet'],
#        '98': ['Which of the following claim is true?',
#               'A firewall with stateless packet filtering policy drops or admits a packet basing the decision on only '
#               'the content of the incoming/outgoing packet'],
#        '99': ['The class c Ipv4 address disting', '(A lot of) network with a smale number of hosts'],
#        '100': ['THE address resolution protocol (ARP) allows to',
#                'Obtain an unknown MAC address a lot host given an Ip address'],
#        '101': ['The TCP header mandatory contains', 'Some flags used for connection set up and fear down'],
#        '102': ['TCP dynamical changes', '[ answer was dropped in cheat sheet ]'],
#        '103': ['the transmission window size to obtain', 'both flow and congestion control'],
#        '104': ['The algorithm that controls the TCP TRANSMISSION window size moves from the slow short phase to the '
#                'congestion avoidance (AIMD)',
#                'When the window size reaches a threshold value'],
#        '105': ['The Ip header mandatory contains', 'source and destination Ip address'],
#        '106': ['THE Domain name system (DNS)',
#                'enables an application to find out the Ip address of a website for which the logical name is known'],
#        '107': ['The network address translation NAT mechanism', 'Can modify the Ip address of packets'],
#        '108': ['The ping program is', 'based on the echo request and echo reply ICMP messages'],
#        '109': ['The through put offered to a traffic flow',
#                'Is given by the lowest throughput offered in all the traversed links i.e the bottleneck'],
#        '110': ['The introduction of subnet masks in the internet  addressing',
#                'Has never been performed due to some scalability    WRONG HAVE BEEN PERFORMED'],
#        '111': ['The congestion window at the beginning of a TCP connection',
#                'Has a size negotiated with the receiver and equal to the maximum value of the receive window    WRONG '
#                'NOT USERS'],
#        '112': ['Only considering the standard features IP router which of the following claims is true',
#                'An IP router uses the ARP protocol to been the IP address of the router to insert as destination  '
#                'address in the IP packet  2ndAn IP router modifies at least one IP addressin the in the packets it '
#                'has to transmit'],
#        '113': ['In a packet switched network the routing is',
#                'The process used for determining the source“ destination routes taken by packets i.e for writing '
#                'the routing table'],
#        '114': ['The transport layer in the internet', 'Provides a reliable data transfer when TCP is used'],
#        '115': ['The destination IP address in an IP packets is',
#                'A fundamental header field used by routers to forward the packets'],
#        '116': ['The congestion control fo the transmission control protocol (TCP) is based',
#                'On the adjustment of the segment to the network conditions'],
#        '117': ['The IP header i.e the IP PCI mandatory contains',
#                'The Time to live (TTL) field that removing from the network packets that were forwarded by too many '
#                'routers'],
#        '118': ['After having identified the correct output port, an ip router',
#                'Modifies the time To live and Header Checksum fields of the datagram header'],
#        '119': ['Which of the following claims is false?',
#                'A host transmits IP packets only to host whose net_id equal to its own net_id'], '120': [
#         'If a router receives an IP packet with correct checksum, TTL=9, and equal IP source and IP destination '
#         'addresses',
#         'It forwards the packet to the destination'],
#        '121': ['An Ethernet switch, when it receives an ARP request packet',
#                'Forward it on all ports, except the over which the packet has been received'],
#        '122': ['During the slow-start phase of the TCP congestion control, the transmission window size of sender',
#                'Doubles at every received acknowledgement'],
#        '123': ['Which of the following features is not performed by the transmission control protocol (TCP)',
#                'In order by  delivery  to the upper layer'],
#        '124': ['Comparing symmetric key cryptography and asymmetric key cryptography, which of the following is true?',
#                'Symmetric algorithms are faster than asymmetric ones'],
#        '125': ['The core of the Internet network', 'Is a network based on mesh of interconnected routers.'],
#        '126': ['The IP version 4 addresses are:',
#                'usually assigned on geographical and topological basis, in order to favor aggregetion']
#        }
TOKEN = ""


dic = {
    '1': ['For a buck power regulator, the output voltage can be', 'lower than or equal to the input voltage'],
    '2': ['A high level sensitive latch has the command LE (latch enable) = 1. In this condition', 'the output changes state following the input'],
    '3': ['A SW implementation of a programmable processor application has', 'lower NRE cost than a dedicated HW'],
    '4': ['In the square wave generator (oscillator) made with a Schmitt trigger inverter, the voltage waveform across the capacitor is', 'exponential'],
    '5': ['In the square wave generator made with a Schmitt trigger inverter, the inverter output voltage is a', 'square wave'],
    '6': ['In a D/A converter with weighed resistances, the values of all weighed resistances have a –2% error. The effect on the D/A characteristic is', 'a gain error'],
    '7': ['A driver with output resistance Ro = Z∞ drives at high level a line with characteristic impedance Z∞ with an open termination and propagation time tp. The transient ends on the entire line', 'after 2 tp'],
    '8': ['The transfer function in continuous current mode of an ideal flyback power regulator depends on', 'the switching duty cycle'],
    '9': ['Which of the variations below does not affect the aliasing signal/noise ratio (SNRa)?', 'Increase of the number of A/D bits'],
    '10': ['A buck-boost power regulator with an inductance', 'its output voltage has inverse polarity to'],
    '11': ['A driver with the output resistance Ro = 2 Z∞ drives at high level (Vdd) a transmission line with the characteristic impedance Z∞ with an adapted termination. The steady-state voltage at the termination end is', 'Vdd / 3'],
    '12': ['A driver with the output resistance RO = Z∞ drives at high level (VOH) a transmission line with the characteristic impedance Z∞, with open termination. At the end of the transient period, the voltage at the termination end is', 'VOH'],
    '13': ['The output circuit is galvanically insulated from the input circuit for', 'flyback power regulators'],
    '14': ['The reflection coefficient of an open termination of a transmission line is', '+1'],
    '15': ['In the square wave generator (oscillator) made with a Schmitt trigger inverter, the voltage wave at the trigger output is', 'square wave'],
    '16': ['The efficiency (ratio of output power/input power) of a linear series regulator with VI input and VO output is approximately', 'VI / VO'],
    '17': ['Bipolar junction transistors operate as switches', 'in saturation region'],
    '18': ['A FLASH NOR memory has, compared to a NAND', 'greater reading speed'],
    '19': ['Suppose that a data acquisition system that uses a 10 bit A/D converter to convert a sine wave signal has SNR = 50 dB. The Effective Number of Bits (ENOB) is about', '8 bits'],
    '20': ['The efficiency of a linear regulator is approximately', 'Vout / Vin'],
    '21': ['An SRAM memory cell includes', '6 MOS'],
    '22': ['A DDR4 memory has the bus clock at 2000 MHz and 8-bit parallelism. The maximum rate is', '32 Gbit/s'],
    '23': ['A CMOS driver with supply voltage Val and output resistance RO drives a line with characteristic impedance Z∞ terminated on an open circuit. The first voltage step (0→1) at the driver exit has the amplitude', 'Val · Z∞ / (RO + Z∞)'],
    '24': ['A CMOS logic gate drives a load of capacity C. By doubling the capacity (2 C), the propagation delay changes as', '2'],
    '25': ['By halving the load capacity of a CMOS logic gate, the dynamic power changes by a factor', '1/2'],
    '26': ['Assuming that the SNR of a data acquisition system using a 10-bit A/D converter is 55.76 dB, the Effective Number of Bits (ENOB) is', '9 bit'],
    '27': ['A boost power regulator injects noise', 'more in the output circuit'],
    '28': ['A voltage regulator using a parallel Zener diode', 'draws constant the current from the power supply'],
    '29': ['A driver with the output resistance Ro = Z∞ drives at high level (Vdd) a line with Z∞ characteristic impedance with an adapted termination. In steady state, the voltage at the termination end is', 'Vdd / 2'],
    '30': ['Compared to a linear regulator, a switching regulator allows to', 'increase the efficiency of the regulator'],
    '31': ['For transistors, “β”', 'is the current gain of the bipolar junction transistors'],
    '32': ['An address decoder with 4-bit input requires', '16 NAND gates'],
    '33': ['An FPGA uses only 4-input Look-up-Table (LUT) to perform combinatorial logic functions. To achieve O = A B C (D + E + F) are needed', '2 LUT'],
    '34': ['A Zener diode', 'can keep constant the voltage across the diode'],
    '35': ['The ripple voltage of a half-wave rectifier is halved if', 'the capacity doubles'],
    '36': ['In a Schmitt trigger oscillator, doubling the value of the capacitor', 'halves the frequency'],
    '37': ['By doubling the frequency of a CMOS logic gate, the dynamic power changes by', '2'],
    '38': ['In the electric model of the thermal paths, the ambient temperature is modeled by', 'a voltage source'],
    '39': ['In a square and triangular wave generator (a circuit with two operational amplifiers), we halve the difference between the comparator thresholds and we double the value of the capacitor. If we do not change any other parameters, then the square wave signal', 'does not change the frequency'],
    '40': ['Suppose that a data acquisition system that uses a 10 bit A/D converter to convert a sine wave signal has the SNR = 56 dB. The Effective Number of Bits (ENOB) is about', '9 bits'],
    '41': ['The voltage gain of a boost voltage regulator with duty cycle D = 0.75 is', '4'],
    '42': ['A metal-oxide-semiconductor transistor works as a switch', 'in the triode region'],
    '43': ['In the Schmitt trigger oscillator, the peak-to-peak amplitude of the voltage on the capacitor', 'is equal to the distance between the two threshold voltages of the Schmitt trigger gate'],
    '44': ['If the non-recurring costs NRE to manufacture an integrated circuit double, in order to keep the cost per product constant, it is generally necessary to', 'double the number of chips sold'],
    '45': ['In the electric model of the thermal paths, the thermal resistance is modeled by', 'a resistor'],
    '46': ['In an oscillator with a Schmitt trigger, if we double the resistor value', 'halves the frequency'],
    '47': ['A high-level sensitive latch has the LE command (latch enable) = 0. In this condition', 'the output does not change even if the input changes'],
    '48': ['A FLASH memory cell includes', 'A floating gate MOS'],
    '49': ['Which of the following conditions implies an incorrect connection between logic gates?', 'IO > | IOH |'],
    '50': ['The voltage gain of a buck regulator with duty cycle D = 0.25 is', '0.25'],
    '51': ['A low level sensitive latch has the LE command (latch enable) = 1. In this condition', 'the output does not change even if the input changes'],
    '52': ['In a full-wave rectifier, compared to a half-wave rectifier', 'the ripple output voltage halves'],
    '53': ['If all the resistances of a D/A converter made with R-2R ladder network are 5% lower than their nominal values, the conversion characteristic has', 'a gain error'],
    '54': ['A FLASH NAND memory has, compared to a NOR', 'greater density'],
    '55': ['The schematic below represents', 'a buck power regulator circuit'],
    '56': ['In a negative edge-triggered flip-flop with asynchronous active low reset (RST), if RST = 0', 'the output always remains at'],
    '57': ['The output (regulated) voltage of an ideal boost power regulator can be', 'Higher or equal to the input voltage'],
    '58': ['A DRAM memory cell includes', 'A MOS transistor and a capacitance'],
    '59': ['By doubling the supply voltage of a CMOS logic gate the dynamic power changes as', '4'],
    '60': ['A group of four analog signals has (for each channel) levels between -1 V and + 1 V, maximum frequency Fmax = 2 kHz. The A/D converter has input dynamic from 0 V to +10 V. The overall sampling frequency Fs is four times the minimum. Calculate the minimum number of bits of the converter for a bipolar quantization error below 0.1%.', '9 bits'],
    '61': ['The transfer function in continuous current mode of an ideal flyback power regulator depends on', 'the characteristics of the electrical transformer'],
    '62': ['A dedicated hardware implementation of an application has', 'lower unit cost than a software using a CPU'],
    '63': ['In a synchronous write cycle, the STB signal must remain high for a minimum delay of', 'Th + Tk'],
    '64': ['The transfer function in continuous current mode of an ideal buck power regulator depends on', 'the switch duty cycle'],
    '65': ['A buck power regulator injects noise', 'more in the input circuit'],
    '66': ['Power derating of electronic devices is due to', 'ambient temperature']
}





import telebot
import random

bot = telebot.TeleBot(TOKEN)

# User state dictionary to track the current question and answer status
user_state = {}


def options(r, ran):
    arr = []
    while len(arr) < 3:
        num = random.randint(1, 65)
        if num != ran:
            arr.append(dic[str(num)][1])

    arr.insert(r - 1, dic[str(ran)][1])
    return arr


t = 30


def questions():
    global t
    t += 1
    if t > 65:
        t = 1
    rand = random.randint(1, 65)
    rand5 = random.randint(1, 3)
    question = {
        'question': str(t) + ' : ' + dic[str(t)][0],
        'options': options(rand5, t),
        'answer': rand5 - 1
    }
    return question


@bot.message_handler(commands=['start'])
def start(message):
    # Present the Give button
    present_give_button(message.chat.id)


def present_give_button(chat_id):
    # Create a keyboard with answer options
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    random_question = questions()
    answer_options = random_question['options']

    # Add answer options as buttons
    for option in answer_options:
        keyboard.add(telebot.types.KeyboardButton(option))

    # Update user state to track the current question and answer status
    user_state[chat_id] = {
        'question': random_question,
        'answered': False
    }

    # Send the question with answer options
    bot.send_message(chat_id, random_question['question'], reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    text = message.text.strip()
    chat_id = message.chat.id

    print([message.chat.username, message.chat.first_name, message.chat.last_name])
    print(message.chat)
    # Check if the user has already answered the question
    user = user_state.get(chat_id)
    if user and not user['answered']:
        user['answered'] = True  # Mark the question as answered

        selected_answer = text
        correct_answer_index = user['question']['answer']
        answer_options = user['question']['options']
        correct_answer = answer_options[correct_answer_index]

        if selected_answer == correct_answer:
            bot.send_message(chat_id, "Correct answer!")
        else:
            bot.send_message(chat_id, f"Wrong answer! The correct answer is: {correct_answer}")

    # Present the next question
    present_give_button(chat_id)


bot.polling()
