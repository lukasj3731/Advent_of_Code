import re


def make_particle(line):
    line = line[2:]
    ret = []
    for vector in line.split(', '):
        coords = re.findall('-?[0-9]+', vector)
        ret.append((int(coords[0]), int(coords[1]), int(coords[2])))
    return ret


def iterate(particle):
    p = particle[0]
    v = particle[1]
    a = particle[2]
    new_v = (v[0]+a[0], v[1]+a[1], v[2]+a[2])
    new_p = (p[0]+new_v[0], p[1]+new_v[1], p[2]+new_v[2])
    return [new_p, new_v, a]


def dist(particle):
    return abs(particle[0][0])+abs(particle[0][1])+abs(particle[0][2])


def solve20():
    particles = []
    for line in open('inputs/day20.txt').read().split('\n'):
        particles.append(make_particle(line))
    for iterations in range(5000):
        for i in range(len(particles)):
            particles[i] = iterate(particles[i])
    min_dist = 999999999
    particle_id = -1
    for i in range(len(particles)):
        d = dist(particles[i])
        if d < min_dist:
            min_dist = d
            particle_id = i
    print(particle_id)