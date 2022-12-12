from stem.descriptor.remote import DescriptorDownloader

downloader = DescriptorDownloader()
descriptors = downloader.get_server_descriptors().run()
for descriptor in descriptors:
  print('Descriptor\n', str(descriptor))
  print('Certificate\n', descriptor.certificate)
  print('Onion key\n', descriptor.onion_key)
  print('Signing key\n', descriptor.signing_key)
  print('Signature\n', descriptor.signature)
  print()

