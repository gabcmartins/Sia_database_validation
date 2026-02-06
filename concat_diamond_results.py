import os
import pandas as pd

dir_base = "/home/gabrielacastilho/Jo/diamond_1_inital"
nome_base = "1_initial"

dfs = []

for arquivo in os.listdir(dir_base):
    if arquivo.endswith("_matches_best_hits.tsv"):
        amostra = arquivo.split("_")[0]
        caminho = os.path.join(dir_base, arquivo)

        df = pd.read_csv(caminho, sep='\t')

        df = df.rename(columns={
            "qseqid": "CDS",
            "sseqid": "Annotation"
        })

        df["Amostra"] = amostra
        df["Database"] = nome_base

        dfs.append(df)

df_cazy = pd.concat(dfs, ignore_index=True)

df_cazy.to_csv(
    "/home/gabrielacastilho/Jo/diamond_1_inital/1_matches_concat.tsv",
    sep="\t",
    index=False
)

print("1 concatenado ✅")
