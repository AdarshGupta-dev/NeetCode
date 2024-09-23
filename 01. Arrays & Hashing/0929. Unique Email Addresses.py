from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        map = set()

        for email in emails:
            # splitting into username and domain 
            local, domain = email.split('@')

            # removing periods as they are not considered part of email.
            local = local.replace(".", "")

            # removing username after + sign, as those are also not considered.
            local = local.split('+')[0]

            # adding stripped email to set
            map.add(local + '@' + domain)

        return len(map)
