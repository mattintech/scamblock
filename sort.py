import re

# Read the input file
with open('hosts_raw.txt', 'r') as file:
    lines = file.readlines()

# Keep lines that start with # or are empty
comment_lines = [line for line in lines if line.strip().startswith('#') or line.strip() == '']

# Extract IP and DNS names from the relevant lines
ip_dns_names = []
for line in lines:
    match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([\w\.]+)', line)
    if match:
        ip_dns_names.append((match.group(1), match.group(2)))

# Group like domains together
domain_groups = {}
for ip, dns_name in ip_dns_names:
    domain = dns_name.split('.')[-2] + '.' + dns_name.split('.')[-1]
    if domain not in domain_groups:
        domain_groups[domain] = []
    domain_groups[domain].append((ip, dns_name))

# Sort DNS names alphabetically within each group, with domains without a host first
for domain in domain_groups:
    domain_groups[domain].sort(key=lambda x: (x[1].split('.')[0] != domain.split('.')[0], x[1]))

# Write the output to a new file
with open('hosts', 'w') as file:
    for line in comment_lines:
        file.write(line)
    for domain in sorted(domain_groups.keys()):
        for ip, dns_name in domain_groups[domain]:
            file.write(f'{ip} {dns_name}\n')