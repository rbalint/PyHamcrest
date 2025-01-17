__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.matcher import Matcher
from hamcrest.core.string_description import tostring


class BaseMatcher(Matcher):
    """Base class for all :py:class:`~hamcrest.core.matcher.Matcher`
    implementations.

    Most implementations can just implement :py:obj:`_matches`, leaving the
    handling of any mismatch description to the ``matches`` method. But if it
    makes more sense to generate the mismatch description during the matching,
    override :py:meth:`~hamcrest.core.matcher.Matcher.matches` instead.

    """

    def __str__(self):
        return tostring(self)

    def _matches(self, item):
        raise NotImplementedError("_matches")

    def matches(self, item, mismatch_description=None):
        match_result = self._matches(item)
        if not match_result and mismatch_description:
            self.describe_mismatch(item, mismatch_description)
        return match_result

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text("was ").append_description_of(item)

    def describe_match(self, item, match_description):
        match_description.append_text("was ").append_description_of(item)
