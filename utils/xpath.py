def xpath_literal(value):
    value = str(value)

    if "'" not in value:
        return f"'{value}'"

    if '"' not in value:
        return f'"{value}"'

    parts = value.split("'")
    quoted_parts = [f"'{part}'" for part in parts]

    return 'concat(' + ', "\'", '.join(quoted_parts) + ')'
