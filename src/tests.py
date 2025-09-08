#!/usr/bin/env uv run

import sys

import pandas as pd


class Tester:
    # fmt: off
    reset = "\033[0m"
    bold  = "\033[1m"
    red   = "\033[31m"
    green = "\033[32m"
    # fmt: on

    def __init__(self, original_list_path: str, ranked_list_path: str) -> None:
        self.original_list_path = original_list_path
        self.ranked_list_path = ranked_list_path

    def _open_csv_or_json(self, path: str) -> pd.DataFrame | None:
        if path.endswith(".csv"):
            with open(path, "r") as f:
                df = pd.read_csv(f)
        elif path.endswith(".json"):
            with open(path, "rb") as f:
                df = pd.read_json(f, orient="records")
        else:
            return None
        return df

    def test_original_drugs(self) -> None:
        # set up testing
        print("TESTING ORIGINAL DRUG LIST")
        has_error = False
        df = self._open_csv_or_json(self.original_list_path)
        if df is None:
            print(f"\tFAIL: Path cannot be opened ({self.original_list_path})")
            sys.exit(
                f"{self.bold}{self.red}Original drug list failed tests. Check the printed information.{self.reset}"
            )

        # test columns
        required_columns = (
            "Canonical Name",
            "Clinician Recommendation",
            "id_type",
            "result_id",
        )
        for required_column in required_columns:
            if required_column not in df.columns:
                has_error = True
                print(f"\tFAIL: Column '{required_column}' missing from original drug list ({self.original_list_path})")

        if has_error:
            sys.exit(
                f"{self.bold}{self.red}Original drug list failed tests. Check the printed information.{self.reset}"
            )
        else:
            print(f"{self.green}PASS{self.reset}")

    def test_ranked_list(self) -> None:
        # set up testing
        print("TESTING RANKED LIST")
        has_error = False
        df = self._open_csv_or_json(self.ranked_list_path)
        if df is None:
            print(f"\tFAIL: Path cannot be opened ({self.ranked_list_path})")
            sys.exit(f"{self.bold}{self.red}Ranked list failed tests. Check the printed information.{self.reset}")

        # load original list
        original_df = self._open_csv_or_json(self.original_list_path)
        if original_df is None:
            print(f"\tFAIL: Path cannot be opened ({self.original_list_path})")
            sys.exit(f"{self.bold}{self.red}Ranked list failed tests. Check the printed information.{self.reset}")

        # test all original drugs are in ranked list
        for result_id in original_df["result_id"]:
            if result_id not in df["result_id"].values:
                has_error = True
                print(
                    f"\tFAIL: {original_df.loc[original_df['result_id'] == result_id, 'Canonical Name'].values[0]} is missing from the ranked list."
                )
            if (df["result_id"] == result_id).sum() > 1:
                has_error = True
                print(
                    f"\tFAIL: {original_df.loc[original_df['result_id'] == result_id, 'Canonical Name'].values[0]} is present multiple times in the ranked list."
                )
        if has_error:
            sys.exit(f"{self.bold}{self.red}Ranked list failed tests. Check the printed information.{self.reset}")

        # make sure names and clinician recommendation are preserved
        for result_id in original_df["result_id"]:
            original_row = original_df["result_id"] == result_id
            ranked_row = df["result_id"] == result_id
            if (
                original_df.loc[original_row, "Clinician Recommendation"].values[0]
                != df.loc[ranked_row, "Clinician Recommendation"].values[0]
            ):
                has_error = True
                print(
                    f"\tFAIL: Non-matching value for 'Clinician Recommendation' for drug {original_df.loc[original_row, 'Canonical Name'].values[0]}"
                )
        if has_error:
            sys.exit(f"{self.bold}{self.red}Ranked list failed tests. Check the printed information.{self.reset}")

        if has_error:
            sys.exit(f"{self.bold}{self.red}Ranked list failed tests. Check the printed information.{self.reset}")
        else:
            print(f"{self.green}PASS{self.reset}")


if __name__ == "__main__":
    test_harness = Tester("data/src/drug_list.csv", "data/ranked.csv")
    test_harness.test_original_drugs()
    test_harness.test_ranked_list()
