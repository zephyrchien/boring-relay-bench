import json

def path(tool: str, proto: str, th: int):
    return '{1}/{0}_{1}_{2}_thread_cpu_mem.txt'.format(
        tool, proto, str(th)
    )

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
            p = path(tool, proto, th)
            v[tool] = extract_mem_from_raw(p)
        res[k] = v
    return res

def main():
    res = {}

    for proto in ['tcp', 'ws', 'wss']:
        res[proto] = extract_mem(proto)
    
    with open('mem.json', 'w+') as fp:
        json.dump(res, fp)


if __name__ == "__main__":
    main()
