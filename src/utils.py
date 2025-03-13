"""Utility functions for the cheetah tutorial notebook."""

import matplotlib.pyplot as plt
import numpy as np


def plot_tuning_history(history: dict, fig=None, figsize=(16, 3)):
    """Plot the gradient-based tuning history."""
    figsize = (16, 3) if fig is None else figsize
    if fig is None:
        fig = plt.figure(figsize=(16, 3))

    ax1 = fig.add_subplot(1, 4, 1)
    ax1.plot(history["loss"])
    # ax1.set_yscale("log")
    ax1.set_xlabel("Iteration")
    ax1.set_ylabel("Loss")
    ax1.set_title("Loss")

    ax2 = fig.add_subplot(1, 4, 2)
    ax2.plot([record[0] for record in history["beam_parameters"]], label="mu_x")
    ax2.plot([record[1] for record in history["beam_parameters"]], label="sigma_x")
    ax2.plot([record[2] for record in history["beam_parameters"]], label="mu_y")
    ax2.plot([record[3] for record in history["beam_parameters"]], label="sigma_y")
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Beam parameter (m)")
    ax2.set_title("Beam parameters")
    ax2.legend()

    ax3 = fig.add_subplot(1, 4, 3)
    ax3.plot([record[0] for record in history["magnet_settings"]], label="AREAMQZM1")
    ax3.plot([record[1] for record in history["magnet_settings"]], label="AREAMQZM2")
    ax3.plot([record[3] for record in history["magnet_settings"]], label="AREAMQZM3")
    ax3.set_xlabel("Iteration")
    ax3.set_ylabel("Quadrupole strength (1/m^2)")
    ax3.set_title("Quadrupole settings")
    ax3.legend()

    ax4 = fig.add_subplot(1, 4, 4)
    ax4.plot([record[2] for record in history["magnet_settings"]], label="AREAMCVM1")
    ax4.plot([record[4] for record in history["magnet_settings"]], label="AREAMCHM1")
    ax4.set_xlabel("Iteration")
    ax4.set_ylabel("Steering angle (rad)")
    ax4.set_title("Steerer settings")
    ax4.legend()

    fig.tight_layout()


def plot_system_identification_training(
    history: dict, ground_truth: np.ndarray | None = None, save_path: str | None = None
) -> None:
    fig, axs = plt.subplots(3, 1, figsize=(3.5, 3.8), sharex=True)

    axs[0].plot(history["loss"])
    axs[0].set_ylabel("Loss")

    axs[1].plot(
        [record[0] * 1e3 for record in history["misalignment_q1"]],
        label=r"$Q_1$",
        linestyle="-",
        c="#FF6F61",
    )
    axs[1].plot(
        [record[0] * 1e3 for record in history["misalignment_q2"]],
        label=r"$Q_2$",
        linestyle="-",
        c="#6B5B95",
    )
    axs[1].plot(
        [record[0] * 1e3 for record in history["misalignment_q3"]],
        label=r"$Q_3$",
        linestyle="-",
        c="#88B04B",
    )
    if ground_truth is not None:
        axs[1].axhline(
            ground_truth[0] * 1e3, color="tab:blue", linestyle="--", c="#FF6F61"
        )
        axs[1].axhline(
            ground_truth[2] * 1e3, color="tab:orange", linestyle="--", c="#6B5B95"
        )
        axs[1].axhline(
            ground_truth[4] * 1e3, color="tab:green", linestyle="--", c="#88B04B"
        )
    axs[1].set_ylabel("x misalignment (mm)")
    axs[1].legend(ncol=3)

    axs[2].plot(
        [record[1] * 1e3 for record in history["misalignment_q1"]],
        label=r"$Q_1$",
        linestyle="-",
        c="#FFD700",
    )
    axs[2].plot(
        [record[1] * 1e3 for record in history["misalignment_q2"]],
        label=r"$Q_2$",
        linestyle="-",
        c="#40E0D0",
    )
    axs[2].plot(
        [record[1] * 1e3 for record in history["misalignment_q3"]],
        label=r"$Q_3$",
        linestyle="-",
        c="#FF7E5F",
    )
    if ground_truth is not None:
        axs[2].axhline(
            ground_truth[1] * 1e3, color="tab:blue", linestyle="--", c="#FFD700"
        )
        axs[2].axhline(
            ground_truth[3] * 1e3, color="tab:orange", linestyle="--", c="#40E0D0"
        )
        axs[2].axhline(
            ground_truth[5] * 1e3, color="tab:green", linestyle="--", c="#FF7E5F"
        )
    axs[2].set_xlabel("Epoch")
    axs[2].set_ylabel("y misalignment (mm)")
    axs[2].legend(ncol=3)

    plt.tight_layout()

    if save_path is not None:
        fig.savefig(save_path)

    plt.show()
