"""
CAC 2024 Quarterly Analysis

Generated with assistance from an LLM (ChatGPT / Codex-style tool).
Contact: 23f3000686@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str = "cac_2024.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def summarize_cac(df: pd.DataFrame):
    avg_cac = df["cac"].mean()
    latest_cac = df["cac"].iloc[-1]
    target = df["industry_target"].iloc[0]

    # quarter-over-quarter deltas
    df["qoq_change"] = df["cac"].diff()

    gap_vs_target = latest_cac - target
    percent_above_target = gap_vs_target / target * 100

    print("=== CAC 2024 Summary ===")
    print(df[["quarter", "cac", "qoq_change"]])
    print()
    print(f"Average CAC 2024: {avg_cac:.2f}")
    print(f"Latest quarter CAC ({df['quarter'].iloc[-1]}): {latest_cac:.2f}")
    print(f"Industry target CAC: {target:.2f}")
    print(f"Gap to target (latest): {gap_vs_target:.2f}")
    print(f"Percent above target (latest): {percent_above_target:.1f}%")

    return {
        "avg_cac": avg_cac,
        "latest_cac": latest_cac,
        "gap_vs_target": gap_vs_target,
        "percent_above_target": percent_above_target,
    }


def plot_trend(df: pd.DataFrame, output_path: str = "cac_trend_2024.png"):
    plt.figure()
    plt.plot(df["quarter"], df["cac"], marker="o")
    plt.title("Customer Acquisition Cost (CAC) - 2024 Quarterly Trend")
    plt.xlabel("Quarter")
    plt.ylabel("CAC")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Saved trend plot to {output_path}")


def plot_vs_target(df: pd.DataFrame, output_path: str = "cac_vs_target_2024.png"):
    plt.figure()
    quarters = df["quarter"]
    cac_values = df["cac"]
    target_values = df["industry_target"]

    # Plot CAC bars
    plt.bar(quarters, cac_values, label="Actual CAC")

    # Plot target line
    plt.plot(quarters, target_values, linestyle="--", marker="x", label="Industry Target (150)")

    plt.title("CAC vs Industry Target - 2024")
    plt.xlabel("Quarter")
    plt.ylabel("CAC")
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Saved benchmark plot to {output_path}")


if __name__ == "__main__":
    df_cac = load_data()
    metrics = summarize_cac(df_cac)
    plot_trend(df_cac)
    plot_vs_target(df_cac)
