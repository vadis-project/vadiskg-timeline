from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from rdflib import URIRef

from vadiskg.kg import KG


def main() -> None:
    data_path = Path("./vadis_kg_2024_08_14.nt")
    kg = KG.load_from_nt(data_path)

    start_year = 2010
    end_year = kg.get_latest_publish_year()
    block_size = 1

    year_blocks = [
        list(range(s, s + block_size)) for s in range(start_year, end_year, block_size)
    ]

    top_k = 100
    target_variables = kg.get_top_k_variables(top_k)
    # target_variables = [
    #     URIRef(
    #         "https://data.gesis.org/vadiskg/resource/variable/exploredata-ZA6900_Varv41"
    #     ),
    #     URIRef(
    #         "https://data.gesis.org/vadiskg/resource/variable/exploredata-ZA4231_Varv272"
    #     ),
    #     URIRef(
    #         "https://data.gesis.org/vadiskg/resource/variable/exploredata-ZA6695_Vard71_2"
    #     ),
    # ]

    data: dict[str, list[str | int]] = {"variable": [], "count": [], "year": []}
    for year_block in year_blocks:
        variables = kg.get_variables_by_publications(
            kg.get_publications_by_years(year_block)
        )
        filtered_variables = [v for v in variables if v in target_variables]
        cnt = Counter(filtered_variables)

        for v in target_variables:
            data["variable"].append(v)
            data["count"].append(cnt[v])
            data["year"].append(year_block[0])

    df = pd.DataFrame.from_dict(data)
    sns.lineplot(data=df, x="year", y="count", hue="variable")
    plt.show()


if __name__ == "__main__":
    main()
