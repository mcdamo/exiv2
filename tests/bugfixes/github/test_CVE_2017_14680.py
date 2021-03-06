# -*- coding: utf-8 -*-

import system_tests


class CVE_2017_14680(system_tests.Case):

    bug_no = "73"
    url = "https://github.com/Exiv2/exiv2/issues/73"

    filename = "{data_path}/003-heap-buffer-over"
    commands = ["{exiv2} " + filename]
    stdout = [""]
    stderr = ["""{exiv2_exception_msg} """ + filename + """:
{error_58_message}
"""]
    retval = [1]
