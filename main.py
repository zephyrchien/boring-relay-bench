import json
import matplotlib.pyplot as plt

GO = '#00ADD8'
RUST = '#dea584'
LINESTYLE = ['-', '--', '-.', ':', '-']

def tcp_mem():
    mem = None
    with open('mem.json') as fp:
        mem = json.load(fp)['tcp']

    plt.figure(figsize=(12, 9))

    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = mem[k]['realm']
        gost = mem[k]['gost']
        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.title('TCP Memory Usage')
    plt.xlabel('Time (500ms)', fontsize=12, loc='right')
    plt.ylabel('Memory (MB)', fontsize =12)
    # plt.show()
    plt.savefig('tcp_mem.png')

def ws_mem():
    mem = None
    with open('mem.json') as fp:
        mem = json.load(fp)['ws']

    plt.figure(figsize=(12, 14))

    plt.subplot(211)
    plt.title('WS Sender Memory Usage')
    plt.xlabel('Time (500ms)', fontsize=12, loc='right')
    plt.ylabel('Memory (MB)', fontsize =12)
    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = mem[k]['realm'][::2]
        gost = mem[k]['gost'][::2]
        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.subplot(212)
    plt.title('WS Receiver Memory Usage')
    plt.xlabel('Time (500ms)', fontsize=12, loc='right')
    plt.ylabel('Memory (MB)', fontsize =12)
    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = mem[k]['realm'][1::2]
        gost = mem[k]['gost'][1::2]
        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    # plt.show()
    plt.savefig('ws_mem.png')

def wss_mem():
    mem = None
    with open('mem.json') as fp:
        mem = json.load(fp)['wss']

    plt.figure(figsize=(12, 14))

    plt.subplot(211)
    plt.title('WSS Sender Memory Usage')
    plt.xlabel('Time (500ms)', fontsize=12, loc='right')
    plt.ylabel('Memory (MB)', fontsize =12)
    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = mem[k]['realm'][::2]
        gost = mem[k]['gost'][::2]
        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    plt.subplot(212)
    plt.title('WSS Receiver Memory Usage')
    plt.xlabel('Time (500ms)', fontsize=12, loc='right')
    plt.ylabel('Memory (MB)', fontsize =12)
    for (idx, th) in enumerate([1, 10, 30, 50, 100]):
        k = 'th' + str(th)
        realm = mem[k]['realm'][1::2]
        gost = mem[k]['gost'][1::2]
        plt.plot(realm, color=RUST, ls=LINESTYLE[idx], label=k)
        plt.plot(gost, color=GO, lw=1.5, ls=LINESTYLE[idx], label=k)
        plt.legend(loc='best')

    # plt.show()
    plt.savefig('wss_mem.png')

tcp_mem()
ws_mem()
wss_mem()