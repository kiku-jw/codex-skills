#!/usr/bin/env python3
import argparse
import re
import sys
from datetime import date
from pathlib import Path


CORE_TEMPLATE_FILES = {
    "prd.md": "prd.md",
    "contracts.md": "contracts.md",
    "schema.sql": "schema.sql",
    "test-plan.md": "test-plan.md",
    "epics.md": "epics.md",
}

ARCHITECTURE_TEMPLATE_FILES = {
    "blueprint.md": "blueprint.md",
    "gate-matrix.md": "gate-matrix.md",
}

ADR_TEMPLATE_FILE = ("adr/0001-decision.md", "adr-template.md")


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "project"


def render_template(text: str, project_name: str, project_slug: str) -> str:
    return (
        text.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{PROJECT_SLUG}}", project_slug)
        .replace("{{TODAY}}", date.today().isoformat())
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold an agent-ready spec bundle.")
    parser.add_argument("--out", required=True, help="Output directory for the bundle.")
    parser.add_argument(
        "--project-name",
        required=True,
        help="Human-readable project name used in template placeholders.",
    )
    parser.add_argument(
        "--project-slug",
        help="Optional explicit slug. Defaults to a slugified project name.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files in the output directory.",
    )
    parser.add_argument(
        "--with-architecture-pack",
        action="store_true",
        help="Include blueprint and gate-matrix templates.",
    )
    parser.add_argument(
        "--with-adrs",
        action="store_true",
        help="Include an ADR template inside adr/.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "templates"
    out_dir = Path(args.out).expanduser().resolve()
    project_slug = args.project_slug or slugify(args.project_name)
    with_architecture_pack = args.with_architecture_pack or args.with_adrs

    out_dir.mkdir(parents=True, exist_ok=True)

    template_files = dict(CORE_TEMPLATE_FILES)
    if with_architecture_pack:
        template_files.update(ARCHITECTURE_TEMPLATE_FILES)
    if args.with_adrs:
        template_files[ADR_TEMPLATE_FILE[0]] = ADR_TEMPLATE_FILE[1]

    created = []
    skipped = []
    for output_name, template_name in template_files.items():
        target = out_dir / output_name
        if target.exists() and not args.force:
            skipped.append(output_name)
            continue
        template_path = template_dir / template_name
        rendered = render_template(
            template_path.read_text(encoding="utf-8"),
            args.project_name,
            project_slug,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
        created.append(output_name)

    summary_lines = [
        f"bundle: {out_dir}",
        f"project_name: {args.project_name}",
        f"project_slug: {project_slug}",
        f"architecture_pack: {'yes' if with_architecture_pack else 'no'}",
        f"adrs: {'yes' if args.with_adrs else 'no'}",
        f"created: {', '.join(created) if created else '-'}",
        f"skipped: {', '.join(skipped) if skipped else '-'}",
    ]
    sys.stdout.write("\n".join(summary_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
