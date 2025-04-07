"""Utility functions for the cheetah tutorial notebook."""

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from xopt import VOCS, Evaluator


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


def plot_parameter_space_difference(
    vocs: VOCS,
    evaluator: Evaluator,
    prior_mean_module: nn.Module,
    num_points: int = 50,
    figsize: tuple = None,
) -> plt.Figure:
    q1 = np.linspace(
        vocs.variables["q1"][0], vocs.variables["q1"][1], num_points, dtype=np.float32
    )
    q2 = np.linspace(
        vocs.variables["q2"][0], vocs.variables["q2"][1], num_points, dtype=np.float32
    )

    X, Y = np.meshgrid(q1, q2)

    Z_problem = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z_problem[i, j] = evaluator.evaluate({"q1": X[i, j], "q2": Y[i, j]})["mae"]
    Z_priormean = (
        prior_mean_module(torch.tensor(np.stack([X, Y], axis=-1), dtype=torch.float32))
        .detach()
        .numpy()
    )

    figsize = (4, 1.8) if figsize is None else figsize
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    v_min = min(Z_problem.min(), Z_priormean.min())
    v_max = max(Z_problem.max(), Z_priormean.max())

    axes[0].contourf(X, Y, Z_problem, levels=20, vmin=v_min, vmax=v_max)
    axes[1].contourf(X, Y, Z_priormean, levels=20, vmin=v_min, vmax=v_max)
    # Mark the minimum for both plots
    idx_min_problem = np.unravel_index(np.argmin(Z_problem, axis=None), Z_problem.shape)
    axes[0].scatter(
        q1[idx_min_problem[1]], q2[idx_min_problem[0]], color="red", marker="x"
    )
    idx_min_priormean = np.unravel_index(
        np.argmin(Z_priormean, axis=None), Z_priormean.shape
    )
    axes[1].scatter(
        q1[idx_min_priormean[1]], q2[idx_min_priormean[0]], color="red", marker="x"
    )

    axes[0].set_title("Optimization Problem")
    axes[1].set_title("Cheetah Prior Mean Model")

    axes[1].set_yticks([])
    axes[0].set_ylabel(r"$k_{Q2}$ (1/m)")
    for ax in axes:
        ax.set_xlabel(r"$k_{Q1}$ (1/m)")

    # Plot colorbar
    fig.subplots_adjust(right=0.9)
    cbar_ax = fig.add_axes([0.95, 0.1, 0.03, 0.8])
    fig.colorbar(
        plt.cm.ScalarMappable(cmap="viridis"), cax=cbar_ax, aspect=30, shrink=0.5
    )
    cbar_ax.set_ylabel("Beam size (mm)")
