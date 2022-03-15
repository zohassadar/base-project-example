import regex


def this_in_that(this: str, that: str) -> str | None:
    """This looks for this in that using regex module with
    no way to configure it

    Parameters
    ----------
    this : str
        This is what you are looking for
    that : str
        This is where you are looking for it

    Returns
    -------
    str | None
        If this is to be found in that, you'll get it

    Raises
    ------
    AssertionError
        If this or that is not a string
    """
    assert isinstance(this, str)
    assert isinstance(that, str)
    if result := regex.search(this, that):
        return result.group()
