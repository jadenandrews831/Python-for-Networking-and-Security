import logging

try:
  open('/path/does/not/exist', 'rb')
except Exception as e:
  logging.error('Failed to open file', exc_info=True)
  logging.exception("Failed to open file")

