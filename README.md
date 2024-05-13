

[![latest release](https://img.shields.io/github/release/mattintech/scamblock)](https://github.com/mattintech/scamblock/releases)
[![license](https://img.shields.io/github/license/mattintech/scamblock)](https://github.com/mattintech/scamblock/blob/master/license.txt)

# ScamBlock 

## Overview
This is a list of DNS addresses associated with known scammer domains. It can be used with tools like Pi-hole to block access to these domains on your network, helping to protect against scams and malicious activities.

**Note:** Using this blocklist is just one tool in defending against scammers. It's important to stay vigilant and use other security measures as well.

## Vision
The goal is to make it more difficult for scammers to use tools to exploit their targets.  

## Usage
To use this blocklist with Pi-hole, follow these steps:

1. Log in to your Pi-hole admin interface.
2. Navigate to Settings > Blocklists.
3. Add the following URL to your blocklist:
'''
https://raw.githubusercontent.com/mattintech/scamblock/master/hosts
'''
4. Click "Save and Update" to apply the changes.
5. Pi-hole will now block DNS requests to the domains listed in the blocklist.

## Disclaimer
While this blocklist aims to help protect against scammers, it may not be comprehensive or up to date. It's recommended to combine it with other security measures and regularly update your blocklist to stay protected.

## Contribution
Please submit feel free to submit a PR and include justification as to why you think the DNS names should be blocked