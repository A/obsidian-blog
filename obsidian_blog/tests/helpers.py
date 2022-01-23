import os
from pyfakefs import fake_filesystem_unittest

patcher = fake_filesystem_unittest.Patcher()

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')

def mount_fixture(fixture_name):
  path = f"{fixture_path}/{fixture_name}"
  patcher.fs.add_real_directory(path)
  os.chdir(path)
  return path

def fakefs_setup():
  patcher.setUp()
  return patcher.fs

def fakefs_teardown():
  patcher.tearDown() 
