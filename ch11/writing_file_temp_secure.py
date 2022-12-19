from tempfile import NamedTemporaryFile

def write_results(results):
  filename = NamedTemporaryFile(delete=False)
  print(filename.name)
  filename.write(results.encode())
  print("Results written to", filename)

write_results('writing in a temp file')
