


def preview(d, max_items=5, max_len=80):
    out = {}
    for i, (k, v) in enumerate(d.items()):
        if i >= max_items:
            break
        v_str = str(v)
        out[k] = v_str if len(v_str) <= max_len else v_str[:max_len] + "..."
    return out