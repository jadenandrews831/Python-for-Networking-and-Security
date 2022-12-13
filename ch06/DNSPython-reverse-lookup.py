import dns.reversename

domain = dns.reversename.from_address('45.55.88.72')
print(domain)
print(dns.reversename.to_address(domain))