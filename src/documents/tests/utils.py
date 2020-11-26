import os
import shutil
import tempfile
from collections import namedtuple

from django.test import override_settings


def setup_directories():

    dirs = namedtuple("Dirs", ())

    dirs.data_dir = tempfile.mkdtemp()
    dirs.scratch_dir = tempfile.mkdtemp()
    dirs.media_dir = tempfile.mkdtemp()
    dirs.consumption_dir = tempfile.mkdtemp()
    dirs.index_dir = os.path.join(dirs.data_dir, "documents", "originals")
    dirs.originals_dir = os.path.join(dirs.media_dir, "documents", "originals")
    dirs.thumbnail_dir = os.path.join(dirs.media_dir, "documents", "thumbnails")
    os.makedirs(dirs.index_dir)
    os.makedirs(dirs.originals_dir)
    os.makedirs(dirs.thumbnail_dir)

    override_settings(
        DATA_DIR=dirs.data_dir,
        SCRATCH_DIR=dirs.scratch_dir,
        MEDIA_ROOT=dirs.media_dir,
        ORIGINALS_DIR=dirs.originals_dir,
        THUMBNAIL_DIR=dirs.thumbnail_dir,
        CONSUMPTION_DIR=dirs.consumption_dir,
        INDEX_DIR=dirs.index_dir
    ).enable()

    return dirs


def remove_dirs(dirs):
    shutil.rmtree(dirs.media_dir, ignore_errors=True)
    shutil.rmtree(dirs.data_dir, ignore_errors=True)
    shutil.rmtree(dirs.scratch_dir, ignore_errors=True)
    shutil.rmtree(dirs.consumption_dir, ignore_errors=True)
