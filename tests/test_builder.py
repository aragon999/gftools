import tempfile
import pytest
import shutil
import os
import subprocess


@pytest.mark.parametrize(
    "fp,font_paths",
    [
        (
            os.path.join("data", "test", "builder", "check_compatibility_ufo_1"),
            [
                os.path.join("ttf", "TestFamily-Black.ttf"),
                os.path.join("ttf", "TestFamily-Thin.ttf"),
                os.path.join("otf", "TestFamily-Black.otf"),
                os.path.join("otf", "TestFamily-Thin.otf"),
            ],
        ),
    ],
)
def test_builder(fp, font_paths):
    with tempfile.TemporaryDirectory() as tmp_dir:
        src_dir = os.path.join(tmp_dir, "sources")
        font_dir = os.path.join(tmp_dir, "fonts")
        shutil.copytree(fp, src_dir)
        build_path = os.path.join(src_dir, "config.yaml")
        subprocess.run(["gftools", "builder", build_path])
        for font_path in font_paths:
            font_path = os.path.join(font_dir, font_path)
            assert os.path.exists(font_path)
