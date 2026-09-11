import os

_ON = os.environ.get("MINISGL_TRACE", "1") == "1"   # set MINISGL_TRACE=0 to silence, e.g. for benchmarks

def trace(event: str, **fields) -> None:
    if not _ON:
        return
    parts = []
    for key, value in fields.items():
        if isinstance(value, (list, tuple)):
            value = ",".join(map(str, value))   # one token per field: uids=0,1,2
        parts.append(f"{key}={value}")
    print(f"[TRACE] {event} " + " ".join(parts), flush=True)