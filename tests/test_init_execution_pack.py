import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "init_execution_pack.py"


def test_init_execution_pack_creates_core_files(tmp_path):
    out_dir = tmp_path / "pack"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--out",
            str(out_dir),
            "--project-name",
            "Launch Rail",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert (out_dir / "AGENTS.md").exists()
    assert (out_dir / "docs" / "PLAN.md").exists()
    assert (out_dir / "docs" / "STATUS.md").exists()
    assert (out_dir / "docs" / "TEST_PLAN.md").exists()
    assert (out_dir / "docs" / "BACKLOG.md").exists()
    assert "project_slug: launch-rail" in result.stdout


def test_init_execution_pack_creates_prompts_and_spec_companion(tmp_path):
    out_dir = tmp_path / "pack"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--out",
            str(out_dir),
            "--project-name",
            "Control Loop",
            "--with-prompts",
            "--with-spec-companion",
            "--with-architecture-pack",
            "--with-adrs",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert (out_dir / "prompts" / "execute.md").exists()
    assert (out_dir / "prompts" / "resume.md").exists()
    assert (out_dir / "prompts" / "review-repair.md").exists()
    assert (out_dir / "prompts" / "blocker-compress.md").exists()
    assert (out_dir / "spec" / "prd.md").exists()
    assert (out_dir / "spec" / "contracts.md").exists()
    assert (out_dir / "spec" / "schema.sql").exists()
    assert (out_dir / "spec" / "test-plan.md").exists()
    assert (out_dir / "spec" / "epics.md").exists()
    assert (out_dir / "spec" / "blueprint.md").exists()
    assert (out_dir / "spec" / "gate-matrix.md").exists()
    assert (out_dir / "spec" / "adr" / "0001-decision.md").exists()
    assert "prompts: yes" in result.stdout
    assert "spec_companion: yes" in result.stdout
    assert "adrs: yes" in result.stdout
