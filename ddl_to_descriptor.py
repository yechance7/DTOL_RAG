import re
import json

def parse_ddl(ddl: str):
    tables = []
    columns = []
    column_types = []
    primary_keys = []

    current_table = None
    col_index = 1  # index 0은 항상 ["*", "*"]

    lines = ddl.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('--'):
            continue

        # 테이블 이름 추출
        match = re.match(r'CREATE TABLE\s+(\w+(?:\.\w+)?)[\s(]', line, re.IGNORECASE)
        if match:
            current_table = match.group(1).split('.')[-1]
            tables.append(current_table)
            continue

        # 컬럼 정의 추출
        col_match = re.match(r'(\w+)\s+([\w()]+)', line)
        if col_match and current_table and not line.lower().startswith("constraint"):
            col_name, col_type = col_match.group(1), col_match.group(2).lower()
            columns.append([current_table, col_name])
            column_types.append(map_type(col_type))
            col_index += 1
            continue

        # PK 추출
        pk_match = re.search(r'PRIMARY KEY\s+\(([\w,\s]+)\)', line, re.IGNORECASE)
        if pk_match:
            pk_cols = [col.strip() for col in pk_match.group(1).split(',')]
            for pk in pk_cols:
                try:
                    idx = columns.index([current_table, pk]) + 1  # +1 because of ["*", "*"]
                    primary_keys.append(idx)
                except ValueError:
                    pass

    return {
        "table_names": tables,
        "column_names": [["*", "*"]] + columns,
        "column_types": ["text"] + column_types,
        "primary_keys": primary_keys,
        "foreign_keys": []
    }

def map_type(sql_type: str) -> str:
    if any(x in sql_type for x in ['int', 'numeric', 'decimal', 'number', 'serial']):
        return "number"
    elif any(x in sql_type for x in ['date', 'time']):
        return "time"
    else:
        return "text"

def build_descriptor(ddl_files: list, db_id: str, output_path: str):
    merged_ddl = ""
    for path in ddl_files:
        with open(path, encoding='utf-8') as f:
            merged_ddl += f.read() + '\n'

    parsed = parse_ddl(merged_ddl)
    descriptor = {
        "db_id": db_id,
        **parsed
    }

    with open(output_path, 'w', encoding='utf-8') as out:
        json.dump(descriptor, out, indent=2, ensure_ascii=False)
    print(f"✅ JSON saved to {output_path}")


# 예시 실행
if __name__ == "__main__":
    ddl_paths = [
        "공정클레임 DDL.txt",
        "필드클레임 DDL.txt",
        "벤더사 품질데이터 DDL.txt",
        "회사정보 DDL.txt"
    ]
    build_descriptor(ddl_paths, db_id="dtol_quality", output_path="dtol_quality_descriptor.json")
