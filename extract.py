import json

def path(tool: str, proto: str, th: int, data: str):
    return '{1}/{0}_{1}_{2}_thread_{3}.txt'.format(
        tool, proto, str(th), data
    )

####################################
def extract_mem_from_raw(path: str):
    cpus = []
    mems = []
    with open(path) as fp:
        for line in fp:
            sp = line.strip().split('    ')
            # percentage
            cpu = float(sp[0][:-1])
            # mb
            mem = float(sp[1].split(' / ')[0][:-3])
            cpus.append(cpu)
            mems.append(mem)
    assert(len(cpus) == len(mems))
    return mems

def extract_mem(proto: str):
    res = {
        'th1': {},
        'th10': {},
        'th30': {},
        'th50': {},
        'th100': {}
    }

    for th in [1, 10, 30, 50, 100]:
        k = 'th' + str(th)
        v = {}
        for tool in ['realm', 'gost']:
            p = path(tool, proto, th, 'cpu_mem')
            v[tool] = extract_mem_from_raw(p)
        res[k] = v
    return res

####################################
def extract_iperf_from_raw_1(path: str):
    res = []
    with open(path) as fp:
        n = 0
        for line in fp:
            n += 1
            if n == 1:
                continue
            if n == 62:
                break
            val = float(line.strip().split('  ')[5].strip().split(' ')[0])
            # MB -> GB
            if val > 50:
                val = val/1000
            res.append(val)
    assert(len(res) == 60)
    res[0] = 0
    return res

def extract_iperf_from_raw_x(path: str):
    res = []
    with open(path) as fp:
        for line in fp:
            if not '[SUM]' in line:
                continue
            if 'sender' in line or 'receiver' in line:
                break
            val = float(line.strip().split('  ')[4].strip().split(' ')[0])
            # MB -> GB
            if val > 50:
                val = val/1000
            res.append(val)
    assert(len(res) == 60)
    res[0] = 0
    return res

def extract_iperf(proto: str):
    res = {
        'th1': {},
        'th10': {},
        'th30': {},
        'th50': {},
        'th100': {}
    }

    for th in [1, 10, 30, 50, 100]:
        k = 'th' + str(th)
        v = {}
        for tool in ['realm', 'gost']:
            p = path(tool, proto, th, 'iperf')
            if th == 1:
                v[tool] = extract_iperf_from_raw_1(p)
            else:
                v[tool] = extract_iperf_from_raw_x(p)
        res[k] = v
    return res

####################################
def dump_mem():
    res = {}
    for proto in ['tcp', 'ws', 'wss']:
        res[proto] = extract_mem(proto)
    
    with open('mem.json', 'w+') as fp:
        json.dump(res, fp)

def dump_iperf():
    res = {}
    for proto in ['tcp', 'ws', 'wss']:
        res[proto] = extract_iperf(proto)

    with open('iperf.json', 'w+') as fp:
        json.dump(res, fp)

def main():
    dump_mem()
    dump_iperf()

if __name__ == "__main__":
    main()
