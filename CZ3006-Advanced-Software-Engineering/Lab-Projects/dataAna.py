import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

# import networkx as nx
# import matplotlib.pylot as plt

data = pd.read_csv('SFlow_Data_1.csv.csv', index_col=False, names=['type', 'flow_agent_addr',
                                                                   'inputPort', 'outputPort', 'src_MAC', 'dst_MAC',
                                                                   'eth_type',
                                                                   'in_vlan', 'out_vlan',
                                                                   'src_IP', 'dst_IP', 'IP_Protocol', 'ip_tos',
                                                                   'ip_ttl', 'src_port',
                                                                   'dst_port',
                                                                   'tcp_flags', 'packet_size', 'IP_size',
                                                                   'sampling_rate'])

print('Loading...\n')

top5talker_ip = data['src_IP'].value_counts()[:5]
print('Top 5 Talkers (IP):')
print(top5talker_ip)
print('\n')

top5_listener = data['dst_IP'].value_counts()[:5]
print('Top 5 Listeners (IP):')
print(top5_listener)
print('\n')

top5_app = data['dst_port'].value_counts()[:5]
print('Top 5 Application Protocols:')
print(top5_app)
print('\n')

t_traffic = data['IP_size'].sum()
print('Total traffic: {} bytes\n'.format(t_traffic))

print('Proportion of TCP and UDP')
udp = data['IP_Protocol'].value_counts()[6]
tcp = data['IP_Protocol'].value_counts()[17]
ip_sum = data['IP_Protocol'].sum()
udpper = udp / ip_sum * 100
tcpper = tcp / ip_sum * 100
print(ip_sum)
print('UDP(6):', udp)
print(round(udpper,2),"%")
print('TCP(17):', tcp)
print(round(tcpper,2),"%")
print('\n')

print('Additional stats:\n')
pairs = {}
for index, row in data.iterrows():
    word1 = row['src_IP'] + '/' + row['dst_IP']
    word2 = row['dst_IP'] + '/' + row['src_IP']
    if word1 in pairs.keys():
        pairs[word1] += 1
    elif word2 in pairs.keys():
        pairs[word2] += 1
    else:
        pairs[word1] = 1

pairs_sorted = sorted([(k, v) for k, v in pairs.items()], key=lambda x: x[1], reverse=True)

print('Top 5 communication pairs:\n{}\n'.format(pairs_sorted[:5]))

G = nx.Graph()
nodes = list(set(data['src_IP'].tolist()+data['dst_IP'].tolist())) #creating nodes
G.add_nodes_from(nodes)
for (p,n) in pairs_sorted:
    G.add_edge(p.split('/')[0], p.split('/')[1], weight=n)
size = []
for node in nodes:
    if G.degree(node, weight='weight')<25:
        #color.append('g')
        size.append(5)
    elif G.degree(node, weight='weight')<50:
        #color.append('b')
        size.append(10)
    elif G.degree(node, weight='weight')<75:
        #color.append('c')
        size.append(15)
    elif G.degree(node, weight='weight')<100:
        #color.append('y')
        size.append(20)
    elif G.degree(node, weight='weight')<125:
        #color.append('m')
        size.append(25)
    else:
        #color.append('r')
        size.append(30)
edges = G.edges()
weights = [G[u][v]['weight']/500 for u,v in edges]
print('Network visualised:\n')
nx.draw_spring(G, node_size=size, node_color=range(len(nodes)), width=weights, cmap=plt.cm.bwr)