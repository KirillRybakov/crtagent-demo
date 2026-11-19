from types import SimpleNamespace

def parse_results(raw: str, query: str):
    """verified is bool: True only when a result block contains ✅."""
    results = []
    blocks = raw.split("\n\n")
    for block in blocks:
        if not block.strip():
            continue
        verified = "✅" in block
        results.append(SimpleNamespace(title=block.strip(), verified=verified))
    return SimpleNamespace(query=query, results=results)
