from numpy import array, linspace
from multiprocessing import Pool, cpu_count
from time import perf_counter
import matplotlib.pyplot as plt

def get_f(a:float=10, b:float=28, c:float=2.667):
    def f(x):
        return array([a*(x[1] - x[0]), x[0]*(b - x[2]) - x[1], x[0]*x[1] - c*x[2]])
    return f

def step(x, f, h:float=1e-2):
    k1 = f(x)
    k2 = f(x + k1*h/2)
    k3 = f(x + k2*h/2)
    k4 = f(x + k3*h)
    return x + (k1 + 2*k2 + 2*k3 + k4)*h/6


def worker(crange):
    print(f"--> Hello! I'm the worker starting at {crange[0]:4.2f}")
    a       = 10.
    b       = 28.
    h       = 1e-2
    steps   = 10000
    points  = []

    for c in crange:
        f    = get_f(a,b,c)
        x0   = array([1.,1.,1.])

        for _ in range(steps):
            x = step(x0,f,h)
            if x[0]*x0[0] <= 0:
                points.append(array([c,x0[2] - x0[0]*(x[2] - x0[2])/(x[0] - x0[0]) ]))
            x0 = x

    print(f"==> The worker starting at {crange[0]:4.2f} just finished!")

    return points

if __name__ == "__main__":

    # Create the arguments to be passed for each worker
    N       = 100
    cpus    = cpu_count()
    c_min   = 0.35
    c_max   = 0.65
    delta   = (c_max - c_min) / cpus
    args    = [linspace(c_min + i * delta, c_min + (i+1) * delta - delta/N, N) for i in range(cpus)]
    ints    = []

    # Start them
    with Pool(cpus) as pool:

        initial_time = perf_counter()
        
        for i in pool.map(worker, args): ints += i 
        ints = array(ints).T

        final_time = perf_counter()
        print(f"Execution time: {final_time-initial_time:.6f} seconds")

        fig = plt.figure(figsize=(7,7), constrained_layout=True)
        ax  = fig.add_subplot(111)#,projection='3d')

        ax.scatter(ints[0],ints[1], s=0.1, marker='.', c='k', alpha=0.5) # type: ignore
        # ax.view_init(elev=0, azim=-90)
        ax.set_xlabel('c')
        ax.set_ylabel('y')
        # ax.set_zlabel('z')
        plt.show()