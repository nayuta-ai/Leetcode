"""
time complexity: O(n*m) (n is length of emails, m is length of emails[i])
space complexity: O(n*m) (n is length of emails, m is length of emails[i])
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Args:
            emails (List[str]): there is email address in emails, the length of emails is one or more and one hundred or less, emails[i]'s length is same
        Returns:
            int: number of actually receive email address
        Raises:
            value error: there is no element in list of emails
        Examples:
            emails = ["alice@test.com","my.alice@test.com","alice+my.alice@test.com"] -> 2
            
        """
        assert emails != [], "there is no email address in emails"
        assert len(emails) <= 100, "out of range in emails"
        for i, email in enumerate(emails):
            local, domain = email.split('@')
            local = local.split('+',1)[0]
            local = local.replace('.','')
            emails[i] = local + '@' + domain
        emails_rev = set(emails)
        return len(emails_rev)