import os

def file_size_restriction(filestorage, max_limit=0):
  # max_limit as a byte
  # filestorage param is request file storage
  filestorage.seek(0, os.SEEK_END)
  if max_limit < filestorage.tell():
    return {"status" : 413, "message": "Flie limit exceed"}
  return {"status" : 200}
