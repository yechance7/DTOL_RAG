# requirements
- 3.11 <= python
- duckdb(optional. for transforming json files)
# how to setup and run
## step1: config t2sql_descriptor.json
notion에 업로드한 t2sql_descritpr.sjon gist를 ./descriptors/default/t2sql_descriptor.json으로 복사헤줍시다.
## step2: convert sql example provided by dtol to projects format
dtol에서 제공한 json포멧이 프로젝트의 answer-query쌍 json format과 일치하지 않기 때문에
변형이 필요함. 저는 간단하게 duckdb를 활용했습니다.
```bash
mkdir -p ./training_data_storage/examples
duckdb
# duckdb에서 아래의 쿼리를 실행. duckdb에서 나오는건 ctrl + d
    COPY(
        SELECT
            messages->>'$[1].content' AS question,
            messages->>'$[2].content' AS sql,
        FROM
            'examples/field_process_claim_data.jsonl'
        UNION
        SELECT
            messages->>'$[1].content' AS question,
            messages->>'$[2].content' AS sql,
        FROM
            'examples/qm_vndr_qlty_data.jsonl'
    ) TO 'training_data_storage/examples/examples.json' (FORMAT json, ARRAY true);
```
## step3: install python dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```
## step4.1: run in cli
train??? or ingress??? data to chroma_db(vectordb)
```bash
python ./cli_ingress.py
```
run text2sql
```bash
python ./cli_infer.py <<< "자연어 쿼리"
```
