import json
import matplotlib.pyplot as plt

GO = '#00ADD8'
RUST = '#dea584'
LINESTYLE = ['-', '--', '-.', ':', '-']

def tcp_iperf():
    iperf = None
    with open('iperf.json') as fp:
        iperf = json.load(fp)['tcp']

    plt.figure(figsize=(12, 9))

    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = iperf[k]['realm']
        gost = iperf[k]['gost']

        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.title('TCP Bandwidth')
    plt.xlabel('Time (1000ms)', fontsize=12, loc='right')
    plt.ylabel('Bandwidth (GB)', fontsize =12)
    # plt.show()
    plt.savefig('tcp_iperf.png')

def ws_iperf():
    iperf = None
    with open('iperf.json') as fp:
        iperf = json.load(fp)['ws']

    plt.figure(figsize=(12, 9))

    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = iperf[k]['realm']
        gost = iperf[k]['gost']

        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.title('WS Bandwidth')
    plt.xlabel('Time (1000ms)', fontsize=12, loc='right')
    plt.ylabel('Bandwidth (GB)', fontsize =12)
    # plt.show()
    plt.savefig('ws_iperf.png')

def wss_iperf():
    iperf = None
    with open('iperf.json') as fp:
        iperf = json.load(fp)['wss']

    plt.figure(figsize=(12, 9))

    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = iperf[k]['realm']
        gost = iperf[k]['gost']

        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.title('WSS Bandwidth')
    plt.xlabel('Time (1000ms)', fontsize=12, loc='right')
    plt.ylabel('Bandwidth (GB)', fontsize =12)
    # plt.show()
    plt.savefig('wss_iperf.png')

tcp_iperf()
ws_iperf()
wss_iperf()
