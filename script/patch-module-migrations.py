from pathlib import Path


PATCHES = [
    {
        "path": Path(
            "/usr/local/lib/python3.11/site-packages/"
            "grievance_social_protection/migrations/"
            "0022_ticketattachment_attachmentmutation.py"
        ),
        "old": "('core', '0032_alter_exportablequerymodel_create_date_and_more'),",
        "new": "('core', '0031_alter_mutationlog_client_mutation_id'),",
    },
]


def patch_file(path, old, new):
    if not path.exists():
        return

    content = path.read_text()
    if old in content:
        path.write_text(content.replace(old, new, 1))
        print(f"Patched migration dependency in {path}")
        return

    if new in content:
        print(f"Migration dependency already patched in {path}")
        return

    raise RuntimeError(f"Unexpected migration dependency in {path}")


for patch in PATCHES:
    patch_file(**patch)
