from numpy import array, linspace
from multiprocessing import Pool, cpu_count

# Lorenz velocity field factory
def get_f(a: float, b: float, c: float):
    def f(x):
        return array([
            a * (x[1] - x[0]),
            x[0] * (b - x[2]) - x[1],
            x[0] * x[1] - c * x[2]
        ])
    return f

# RK4 integrator
def step(x, f, h: float = 1e-2):
    k1 = f(x)
    k2 = f(x + k1 * h / 2)
    k3 = f(x + k2 * h / 2)
    k4 = f(x + k3 * h)
    return x + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6

def stepfor(x, f, h: float = 1e-2, nsteps: int = 100):
    for _ in range(nsteps):
        x = step(x, f, h)
    return x

# IMPORTANT: worker must be top-level function
def worker(args):
    x, a, b, c, h, nsteps = args
    f = get_f(a, b, c)  # defined inside worker; not pickled
    return stepfor(x, f, h=h, nsteps=nsteps)

def main():
    # smaller test grid first!
    init = linspace(0, 50, 100)
    initial_points = [array([x, y, z]) for x in init for y in init for z in init]

    a, b, c = 10.0, 28.0, 2.667
    h = 1e-3
    nsteps = 10

    tasks = [(x0, a, b, c, h, nsteps) for x0 in initial_points]

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(worker, tasks)

    print("Computed", len(results), "final states")

if __name__ == "__main__":
    main()
