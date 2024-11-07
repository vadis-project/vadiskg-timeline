from collections import Counter
from pathlib import Path

import pandas as pd
import streamlit as st
from rdflib import URIRef

from vadiskg.kg import KG


@st.cache_data
def load_kg() -> KG:
    data_path = Path("./data/vadis_kg_2024_08_14.nt")
    kg = KG.load_from_nt(data_path)
    return kg


@st.cache_data
def get_latest_publish_year(_kg: KG) -> int:
    return _kg.get_latest_publish_year()


@st.cache_data
def get_all_variables(_kg: KG) -> list[URIRef]:
    return list(set(_kg.get_all_variables()))


if __name__ == "__main__":
    kg = load_kg()

    start_year = 2010
    end_year = get_latest_publish_year(kg)
    block_size = 1

    year_blocks = [
        list(range(s, s + block_size)) for s in range(start_year, end_year, block_size)
    ]

    top_k = 5
    top_variables = kg.get_top_k_variables(top_k)
    all_variables = get_all_variables(kg)

    var_id2text = {vid: kg.variable_id_to_text(vid) for vid in all_variables}
    var_text2id = {v: k for k, v in var_id2text.items()}

    top_variable_texts = [var_id2text[v] for v in top_variables]
    all_variable_texts = [var_id2text[v] for v in all_variables]

    selected_variable_texts = st.multiselect(
        "Select target variables",
        all_variable_texts,
        top_variable_texts,
    )
    selected_variables = [var_text2id[v] for v in selected_variable_texts]

    data: dict[str, list[str | int]] = {"variable": [], "count": [], "year": []}
    for year_block in year_blocks:
        variables = kg.get_variables_by_publications(
            kg.get_publications_by_years(year_block)
        )
        filtered_variables = [v for v in variables if v in selected_variables]
        filtered_variable_texts = [var_id2text[v] for v in filtered_variables]
        cnt = Counter(filtered_variable_texts)

        for v in top_variable_texts:
            data["variable"].append(v)
            data["count"].append(cnt[v])
            data["year"].append(year_block[0])

    df = pd.DataFrame.from_dict(data)
    st.line_chart(data=df, x="year", y="count", color="variable")
