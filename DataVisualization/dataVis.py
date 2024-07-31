from Parameters import *
import numpy as np
import matplotlib.pyplot as plt

for particle_index in range(PARTICLE_NUMBER):
    z, gen_t, gen_x, gen_y, gen_v, gen_xz, gen_yz, pre_t, pre_st, pre_x, pre_sx, pre_y, pre_sy, pre_v, pre_sv, pre_xz, pre_sxz, pre_yz, pre_syz, fil_t, fil_st, fil_x, fil_sx, fil_y, fil_sy,fil_v, fil_sv, fil_xz, fil_sxz, fil_yz, fil_syz, smo_t, smo_st, smo_x, smo_sx, smo_y, smo_sy, smo_v, smo_sv, smo_xz, smo_sxz, smo_yz, smo_syz = np.loadtxt(f"../data/Particle {particle_index}.csv", skiprows=2, unpack=True, delimiter=",", dtype=float)

    figure_t, ax_t = plt.subplots()
    ax_t.grid()
    ax_t.set_xlabel("Z [m]")
    ax_t.set_ylabel("t [s]")
    # t_max = np.max(np.abs(gen_t))
    # ax_t.set_ylim([-t_max*1.3,t_max*1.3])
    ax_t.errorbar(z, gen_t, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_t.errorbar(z[3:], pre_t[3:], yerr=pre_st[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_t.errorbar(z[2:], fil_t[2:], yerr=fil_st[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_t.errorbar(z, smo_t, yerr=smo_st, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_t.legend()
    figure_t.savefig(f"Particle {particle_index} t.pdf")
    plt.close(figure_t)

    figure_x, ax_x = plt.subplots()
    ax_x.grid()
    ax_x.set_xlabel("Z [m]")
    ax_x.set_ylabel("x [m]")
    # x_max = np.max(np.abs(gen_x))
    # ax_x.set_ylim([-x_max*1.3,x_max*1.3])
    ax_x.errorbar(z, gen_x, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_x.errorbar(z[3:], pre_x[3:], yerr=pre_sx[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_x.errorbar(z[2:], fil_x[2:], yerr=fil_sx[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_x.errorbar(z, smo_x, yerr=smo_sx, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_x.legend()
    figure_x.savefig(f"Particle {particle_index} x.pdf")
    plt.close(figure_x)

    figure_y, ax_y = plt.subplots()
    ax_y.grid()
    ax_y.set_xlabel("Z [m]")
    ax_y.set_ylabel("y [m]")
    ax_y.errorbar(z, gen_y, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_y.errorbar(z[3:], pre_y[3:], yerr=pre_sy[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_y.errorbar(z[2:], fil_y[2:], yerr=fil_sy[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_y.errorbar(z, smo_y, yerr=smo_sy, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_y.legend()
    figure_y.savefig(f"Particle {particle_index} y.pdf")
    plt.close(figure_y)

    figure_v, ax_v = plt.subplots()
    ax_v.grid()
    ax_v.set_xlabel("Z [m]")
    ax_v.set_ylabel("v [m/s]")
    # v_max = np.max(np.abs(gen_v))
    # ax_v.set_ylim([-v_max*1.3,v_max*1.3])
    ax_v.errorbar(z, gen_v, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_v.errorbar(z[3:], pre_v[3:], yerr=pre_sv[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_v.errorbar(z[2:], fil_v[2:], yerr=fil_sv[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_v.errorbar(z, smo_v, yerr=smo_sv, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_v.legend()
    figure_v.savefig(f"Particle {particle_index} v.pdf")
    plt.close(figure_v)

    figure_xz, ax_xz = plt.subplots()
    ax_xz.grid()
    ax_xz.set_xlabel("Z [m]")
    ax_xz.set_ylabel("xz [s]")
    # xz_max = np.max(np.abs(gen_xz))
    # ax_xz.set_ylim([-xz_max*1.3,xz_max*1.3])
    ax_xz.errorbar(z, gen_xz, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_xz.errorbar(z[3:], pre_xz[3:], yerr=pre_sxz[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_xz.errorbar(z[2:], fil_xz[2:], yerr=fil_sxz[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_xz.errorbar(z, smo_xz, yerr=smo_sxz, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_xz.legend()
    figure_xz.savefig(f"Particle {particle_index} xz.pdf")
    plt.close(figure_xz)

    figure_yz, ax_yz = plt.subplots()
    ax_yz.grid()
    ax_yz.set_xlabel("Z [m]")
    ax_yz.set_ylabel("yz []")
    ax_yz.errorbar(z, gen_yz, ls=" ", fmt="o", elinewidth=1, capsize=1, label="generated", color="black")
    ax_yz.errorbar(z[3:], pre_yz[3:], yerr=pre_syz[3:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="predicted", color="red")
    ax_yz.errorbar(z[2:], fil_yz[2:], yerr=fil_syz[2:], ls=" ", fmt="o", elinewidth=1, capsize=1, label="filtered", color="blue")
    ax_yz.errorbar(z, smo_yz, yerr=smo_syz, ls=" ", fmt="o", elinewidth=1, capsize=1, label="smoothed", color="green")
    ax_yz.legend()
    figure_yz.savefig(f"Particle {particle_index} yz.pdf")
    plt.close(figure_yz)
