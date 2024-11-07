from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import networkx as nx
from networkx.classes.graph import Graph as XGraph
from rdflib import Graph, Literal, URIRef
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph


@dataclass
class KG:
    XG: XGraph
    G: Graph

    @classmethod
    def load_from_nt(cls, fpath: Path) -> "KG":
        g = Graph()
        g.parse(fpath)
        return cls(rdflib_to_networkx_graph(g), g)

    def compute_centrality_score(self, item_key: str) -> float:
        return cast(float, nx.degree_centrality(self.XG)[item_key])

    def top_k_central_items(self, k: int) -> list[tuple[str, float]]:
        return sorted(nx.degree_centrality(self.XG).items(), key=lambda x: x[-1])[-k:]

    def get_publications_by_years(self, years: list[int]) -> list[URIRef]:
        filtered_publications: list[URIRef] = []

        predicate = URIRef("https://schema.org/datePublished")
        for year in years:
            year_literal = Literal(str(year))
            filtered_publications += self.G.subjects(
                predicate=predicate, object=year_literal
            )

        return filtered_publications

    def get_variables_by_publications(self, publications: list[URIRef]) -> list[URIRef]:
        filtered_sentences: list[URIRef] = []
        predicate = URIRef("https://data.gesis.org/gesiskg/schema/variableReference")
        for pub in publications:
            filtered_sentences += self.G.objects(subject=pub, predicate=predicate)

        variables: list[URIRef] = []
        predicate = URIRef("https://data.gesis.org/vadiskg/schema/detectedVariable")
        for sent in filtered_sentences:
            variables += self.G.objects(subject=sent, predicate=predicate)

        return variables

    def get_all_variables(self) -> list[URIRef]:
        return list(
            self.G.objects(
                predicate=URIRef(
                    "https://data.gesis.org/vadiskg/schema/detectedVariable"
                )
            )
        )

    def get_top_k_variables(self, k: int) -> list[URIRef]:
        predicate = URIRef("https://data.gesis.org/vadiskg/schema/detectedVariable")
        all_variable = self.G.objects(predicate=predicate)
        return [v for v, _ in Counter(all_variable).most_common(k)]

    def get_oldest_publish_year(self) -> int:
        return min(
            [
                int(y)
                for y in self.G.objects(
                    predicate=URIRef("https://schema.org/datePublished")
                )
            ]
        )

    def get_latest_publish_year(self) -> int:
        return max(
            [
                int(y)
                for y in self.G.objects(
                    predicate=URIRef("https://schema.org/datePublished")
                )
            ]
        )

    def variable_id_to_text(self, variable: URIRef | str) -> str:
        if isinstance(variable, str):
            variable = URIRef(variable)
        return str(
            list(
                self.G.objects(
                    subject=variable,
                    predicate=URIRef(
                        "http://rdf-vocabulary.ddialliance.org/discovery#questionText"
                    ),
                )
            )[0]
        )
